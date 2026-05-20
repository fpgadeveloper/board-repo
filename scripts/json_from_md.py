"""Parse canonical entity markdown files into JSON.

Strict but tolerant:
- Front-matter must be valid YAML and contain the required identity fields
  for the entity type. Failure = hard error.
- Bullets in known sections must match the canonical grammar from
  MARKDOWN_FORMAT.md (in this repo). Unrecognized bullets are surfaced as
  warnings; the bullet stays in the markdown for the next pass.
- `## Extras` and `## Notes` are never parsed into JSON. Extras bullets
  are captured separately; Notes is the raw body text.
- Unknown section headings are preserved as warnings, not errors.

This is the canonical strict parser. It lives in the board-repo so the
repo is self-validating (.github/workflows/validate.yml runs it directly).
The website's scripts/build.py imports it from this submodule path.

CLI:
    python scripts/json_from_md.py path/to/file.md   # parse one file, print JSON
    python scripts/json_from_md.py --check boards/    # parse a tree, report issues
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required; pip install pyyaml")


# ============================================================================
# Constants
# ============================================================================

PATH_TO_ENTITY_TYPE = {
    "boards": "standalone",
    "soms": "som",
    "carriers": "carrier",
    "kits": "kit",
    "fmc-cards": "fmc_card",
}

REQUIRED_FRONT_MATTER = {
    "standalone": ["mpn", "name", "status", "url", "vendor", "price", "device"],
    "som":        ["mpn", "name", "status", "url", "vendor", "price", "device"],
    "carrier":    ["mpn", "name", "status", "url", "vendor", "price"],
    "kit":        ["mpn", "name", "status", "url", "vendor", "price", "composition"],
    "fmc_card":   ["mpn", "name", "status", "url", "vendor", "price", "connector_type"],
}

OPTIONAL_FRONT_MATTER = {
    "fmc_card": ["vadj_min", "vadj_max"],
}

# Section heading → JSON key (for sections that map to a top-level JSON field)
SECTION_HEADING_TO_KEY = {
    "Memory": "memory",
    "Flash": "flash",
    "EEPROM": "eeprom",
    "Analog": "analog",
    "Sensors": "sensors",
    "Audio": "audio",
    "Clocking": "clocking",
    "PCIe": "pcie",
    "M.2": "m2",
    "High-speed I/O": "high_speed_io",
    "Video": "video",
    "Display": "display",
    "Networking": "networking",
    "Serial": "serial",
    "USB": "usb",
    "USB UART/JTAG": "usb_bridge",
    "Expansion": "expansion",
    "Storage": "storage",
    "User I/O": "user_io",
    "Wireless": "wireless",
    "Features": "features",
}


# ============================================================================
# ParseResult + helpers
# ============================================================================

@dataclass
class ParseResult:
    data: dict
    notes: str | None = None
    extras: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    unknown_sections: list[str] = field(default_factory=list)


def parse_size(s):
    """'2GB' -> 2048; '32MB' -> 32; '2560MB' -> 2560."""
    if s.endswith("GB"):
        return int(s[:-2]) * 1024
    if s.endswith("MB"):
        return int(s[:-2])
    raise ValueError(f"can't parse size: {s!r}")


def parse_number(s):
    """Parse an int or float, preserving type the way the source JSON would."""
    if "." in s:
        return float(s)
    return int(s)


def warn(warnings, line, msg):
    warnings.append(f"line {line}: {msg}" if line else msg)


# ============================================================================
# Front-matter
# ============================================================================

_FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def split_front_matter(md_text):
    """Return (front_matter_dict, body_text, front_matter_end_line)."""
    m = _FRONT_MATTER_RE.match(md_text)
    if not m:
        raise ValueError("missing or malformed front-matter (must start with `---`)")
    fm = yaml.safe_load(m.group(1))
    if not isinstance(fm, dict):
        raise ValueError("front-matter must be a YAML mapping")
    body = md_text[m.end():]
    end_line = m.group(0).count("\n") + 1
    return fm, body, end_line


def validate_front_matter(fm, entity_type, warnings):
    required = REQUIRED_FRONT_MATTER.get(entity_type)
    if required is None:
        raise ValueError(f"unknown entity_type: {entity_type!r}")
    for key in required:
        if key not in fm:
            raise ValueError(f"front-matter missing required field: {key!r}")
    allowed = set(required) | set(OPTIONAL_FRONT_MATTER.get(entity_type, []))
    for key in fm:
        if key not in allowed:
            warn(warnings, None, f"front-matter has unknown field: {key!r}")


# ============================================================================
# Section splitter
# ============================================================================

_SECTION_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)


def split_sections(body, body_start_line):
    """Split body into (heading, content_lines, heading_line_no) blocks.

    A new section starts at any line matching ^## (exactly two #'s + space).
    `### Subheading` lines do NOT start a new top-level section.
    """
    sections = []
    matches = list(_SECTION_RE.finditer(body))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        # heading line number, 1-based
        before = body[: m.start()]
        heading_line = body_start_line + before.count("\n")
        # content between this heading and the next
        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[content_start:content_end]
        sections.append((heading, content, heading_line))
    return sections


def extract_bullets(content):
    """Pull '- ...' bullets from a section body. Returns list of (text, line_offset)."""
    bullets = []
    for i, line in enumerate(content.splitlines()):
        stripped = line.lstrip()
        if stripped.startswith("- "):
            bullets.append((stripped[2:].rstrip(), i))
    return bullets


# ============================================================================
# Section parsers
# ============================================================================

MEMORY_RE = re.compile(
    r"^(\S+) "
    r"(\d+(?:GB|MB))"
    r"(?: (\d+)-bit)?"
    r"( ECC)?"
    r"(?: (SODIMM|DIMM|UDIMM|RDIMM|LRDIMM))?"
    r"$"
)


def parse_memory(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        m = MEMORY_RE.match(text)
        if not m:
            warn(warnings, base_line + off, f"Memory: unrecognized {text!r}")
            continue
        item = {"type": m.group(1), "size_mb": parse_size(m.group(2))}
        if m.group(3):
            item["width_bits"] = int(m.group(3))
        if m.group(4):
            item["ecc"] = True
        if m.group(5):
            item["form_factor"] = m.group(5).lower()
        items.append(item)
    return items


FLASH_RE = re.compile(
    r"^(\S+) "
    r"(\d+(?:GB|MB))"
    r"(?: (\d+)-bit)?"
    r"$"
)


def parse_flash(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        m = FLASH_RE.match(text)
        if not m:
            warn(warnings, base_line + off, f"Flash: unrecognized {text!r}")
            continue
        item = {"type": m.group(1), "size_mb": parse_size(m.group(2))}
        if m.group(3):
            item["width_bits"] = int(m.group(3))
        items.append(item)
    return items


_EEPROM_LONG = {"MAC": "mac_address", "UID": "unique_id", "ID": "board_id", "data": "user_data"}
_EEPROM_INTERFACES = {"I2C", "SPI", "1-Wire"}


def parse_eeprom(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if not toks:
            warn(warnings, base_line + off, "EEPROM: empty bullet")
            continue
        purposes_tok = toks[0]
        try:
            purposes = [_EEPROM_LONG[p] for p in purposes_tok.split("+")]
        except KeyError as e:
            warn(warnings, base_line + off, f"EEPROM: unknown purpose code {e}")
            continue
        item = {"purpose": purposes}
        for t in toks[1:]:
            if t in _EEPROM_INTERFACES:
                item["interface"] = t
            elif re.fullmatch(r"\d+Kbit", t):
                item["size_kbits"] = int(t[:-4])
            else:
                if "part" in item:
                    warn(warnings, base_line + off, f"EEPROM: extra unrecognized token {t!r}")
                else:
                    item["part"] = t
        items.append(item)
    return items


_ANALOG_LABEL_TO_KEY = {"ADC": "adc", "DAC": "dac", "RF": "rf_transceiver", "AFE": "afe"}


def parse_analog(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if not toks:
            continue
        role = _ANALOG_LABEL_TO_KEY.get(toks[0])
        if role is None:
            warn(warnings, base_line + off, f"Analog: unknown role {toks[0]!r}")
            continue
        item = {"role": role}
        for t in toks[1:]:
            if re.fullmatch(r"\d+ch", t):
                item["channels"] = int(t[:-2])
            elif re.fullmatch(r"\d+-bit", t):
                item["resolution_bits"] = int(t[:-4])
            elif re.fullmatch(r"\d+(?:\.\d+)?MSPS", t):
                item["sample_rate_msps"] = parse_number(t[:-4])
            elif re.fullmatch(r"\d+(?:\.\d+)?-\d+(?:\.\d+)?MHz", t):
                fmin_s, fmax_s = t[:-3].split("-")
                item["frequency_min_mhz"] = parse_number(fmin_s)
                item["frequency_max_mhz"] = parse_number(fmax_s)
            else:
                if "part" in item:
                    warn(warnings, base_line + off, f"Analog: extra unrecognized token {t!r}")
                else:
                    item["part"] = t
        items.append(item)
    return items


_SENSOR_LABEL_TO_KEY = {
    "IMU": "imu", "Accelerometer": "accelerometer", "Gyroscope": "gyroscope",
    "Magnetometer": "magnetometer", "Temperature": "temperature",
    "Pressure": "pressure", "Humidity": "humidity", "Light": "light",
    "Proximity": "proximity", "Microphone": "microphone",
    "Camera": "camera",
}


def parse_sensors(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if not toks:
            continue
        stype = _SENSOR_LABEL_TO_KEY.get(toks[0])
        if stype is None:
            warn(warnings, base_line + off, f"Sensors: unknown type {toks[0]!r}")
            continue
        item = {"type": stype}
        if len(toks) > 1:
            item["part"] = " ".join(toks[1:])
        items.append(item)
    return items


_AUDIO_COUNT_FIELDS = {
    "Line in": "line_in", "Line out": "line_out",
    "Headphone": "headphone_jack", "Microphone": "microphone",
}


def parse_audio(bullets, base_line, warnings):
    data = {}
    for text, off in bullets:
        if text.startswith("Codec "):
            data["codec"] = text[len("Codec "):]
            continue
        if text == "Speaker":
            data["speaker"] = True
            continue
        m = re.match(r"^(Line in|Line out|Headphone|Microphone) x(\d+)$", text)
        if m:
            data[_AUDIO_COUNT_FIELDS[m.group(1)]] = int(m.group(2))
            continue
        warn(warnings, base_line + off, f"Audio: unrecognized {text!r}")
    return data


def parse_clocking(bullets, base_line, warnings):
    data = {}
    for text, off in bullets:
        if text == "Programmable":
            data["programmable"] = True
        elif text == "GPSDO":
            data["gps_disciplined"] = True
        elif m := re.match(r"^SMA clock in x(\d+)$", text):
            data["sma_clock_in"] = int(m.group(1))
        elif m := re.match(r"^SMA clock out x(\d+)$", text):
            data["sma_clock_out"] = int(m.group(1))
        else:
            warn(warnings, base_line + off, f"Clocking: unrecognized {text!r}")
    return data


_PCIE_TYPES = {"Edge", "Slot", "PCIe/104", "iPass", "MCIO", "MiniPCIe-Half", "MiniPCIe-Full"}

PCIE_RE = re.compile(
    r"^(Edge|Slot|PCIe/104|iPass|MCIO|MiniPCIe-Half|MiniPCIe-Full)"
    r"(?: Gen(\d+))?"
    r"(?: x(\d+))?"
    r"( \+mSATA)?"
    r"$"
)


def parse_pcie(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        m = PCIE_RE.match(text)
        if not m:
            warn(warnings, base_line + off, f"PCIe: unrecognized {text!r}")
            continue
        item = {"type": m.group(1)}
        if m.group(2):
            item["gen"] = int(m.group(2))
        if m.group(3):
            item["lanes"] = int(m.group(3))
        if m.group(4):
            item["msata_capable"] = True
        items.append(item)
    return items


_M2_KEYS = {"M-key", "E-key", "B-key", "B+M-key"}
_M2_DEFAULT_IFACES = {
    "M-key": ["PCIe"], "B+M-key": ["PCIe"],
    "E-key": ["PCIe", "USB"], "B-key": ["USB"],
}
_M2_LENGTHS = {"2230", "2242", "2260", "2280", "22110"}
_M2_IFACE_VALUES = {"PCIe", "SATA", "USB"}


def parse_m2(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if not toks or toks[0] not in _M2_KEYS:
            warn(warnings, base_line + off, f"M.2: unrecognized key in {text!r}")
            continue
        item = {"key": toks[0], "direction": "socket"}
        i = 1
        # optional (FF)
        if i < len(toks) and toks[i] == "(FF)":
            item["direction"] = "form-factor"
            i += 1
        # optional interfaces (a single +-joined token, only if non-default)
        explicit_interfaces = False
        if i < len(toks):
            t = toks[i]
            parts = t.split("+")
            if parts and all(p in _M2_IFACE_VALUES for p in parts):
                item["interfaces"] = parts
                explicit_interfaces = True
                i += 1
        # restore default interfaces when absent (emitter omits when matches default)
        if not explicit_interfaces:
            item["interfaces"] = list(_M2_DEFAULT_IFACES[item["key"]])
        # optional Gen<N>
        if i < len(toks) and (m := re.fullmatch(r"Gen(\d+)", toks[i])):
            item["gen"] = int(m.group(1))
            i += 1
        # optional x<lanes>
        if i < len(toks) and (m := re.fullmatch(r"x(\d+)", toks[i])):
            item["lanes"] = int(m.group(1))
            i += 1
        # optional length
        if i < len(toks) and toks[i] in _M2_LENGTHS:
            item["length"] = toks[i]
            i += 1
        if i < len(toks):
            warn(warnings, base_line + off, f"M.2: extra unrecognized tokens in {text!r}: {toks[i:]}")
            continue
        items.append(item)
    return items


def _parse_count_section(bullets, base_line, warnings, section_name, label_map):
    """Generic helper for `## Section\n- <Label> xN`-style sections.
    label_map: ordered list of (label, json_key, requires_count) tuples.
    requires_count=False handles boolean fields ('WiFi', 'Bluetooth')."""
    data = {}
    by_label = {label: (key, requires_count) for label, key, requires_count in label_map}
    for text, off in bullets:
        if text in by_label:
            key, requires_count = by_label[text]
            if requires_count:
                warn(warnings, base_line + off, f"{section_name}: missing count in {text!r}")
                continue
            data[key] = True
            continue
        m = re.match(r"^(.+) x(\d+)$", text)
        if m and m.group(1) in by_label:
            key, _ = by_label[m.group(1)]
            data[key] = int(m.group(2))
            continue
        warn(warnings, base_line + off, f"{section_name}: unrecognized {text!r}")
    return data


_HSI_LABELS = [
    ("SMA transceiver pairs", "sma_transceiver_pairs", True),
    ("Samtec FireFly", "firefly", True),
    ("SlimSAS", "slimsas", True),
    ("Mini-DP transceiver", "displayport_transceiver", True),
]


def parse_high_speed_io(bullets, base_line, warnings):
    return _parse_count_section(bullets, base_line, warnings, "High-speed I/O", _HSI_LABELS)


_VIDEO_LABELS = [
    ("HDMI In", "hdmi_in", True), ("HDMI Out", "hdmi_out", True),
    ("DisplayPort", "displayport", True),
    ("SDI In", "sdi_in", True), ("SDI Out", "sdi_out", True),
    ("AES3 In", "aes_in", True), ("AES3 Out", "aes_out", True),
    ("MIPI DSI", "mipi_dsi", True), ("MIPI CSI", "mipi_csi", True),
    ("VGA Out", "vga_out", True),
]


def parse_video(bullets, base_line, warnings):
    return _parse_count_section(bullets, base_line, warnings, "Video", _VIDEO_LABELS)


def parse_display(bullets, base_line, warnings):
    data = {}
    for text, off in bullets:
        m = re.match(r"^Character LCD (\d+x\d+)$", text)
        if m:
            data["character_lcd"] = m.group(1); continue
        m = re.match(r"^OLED (\d+x\d+)$", text)
        if m:
            data["oled"] = m.group(1); continue
        warn(warnings, base_line + off, f"Display: unrecognized {text!r}")
    return data


_ETH_LABEL_TO_SPEED = {
    "10Mbps": 10, "100Mbps": 100, "1GbE": 1000, "2.5GbE": 2500,
    "5GbE": 5000, "10GbE": 10000, "25GbE": 25000, "40GbE": 40000, "100GbE": 100000,
}
_CAGE_LABEL_TO_KEY = {
    "SFP": "sfp", "SFP+": "sfp_plus", "SFP28": "sfp28", "SFP56": "sfp56", "SFP-DD": "sfp_dd",
    "QSFP": "qsfp", "QSFP+": "qsfp_plus", "QSFP28": "qsfp28", "QSFP56": "qsfp56",
    "QSFP-DD": "qsfp_dd", "QSFP-DD800": "qsfp_dd800",
    "OSFP": "osfp", "OSFP-XD": "osfp_xd",
    "CFP": "cfp", "CFP2": "cfp2", "CFP4": "cfp4", "CFP8": "cfp8",
}


def parse_networking(bullets, base_line, warnings):
    data = {}
    ethernet = []
    for text, off in bullets:
        m = re.match(r"^(\S+) x(\d+)$", text)
        if not m:
            warn(warnings, base_line + off, f"Networking: unrecognized {text!r}")
            continue
        label, count_s = m.group(1), m.group(2)
        if label in _ETH_LABEL_TO_SPEED:
            ethernet.append({"speed": _ETH_LABEL_TO_SPEED[label], "ports": int(count_s)})
        elif label in _CAGE_LABEL_TO_KEY:
            data[_CAGE_LABEL_TO_KEY[label]] = int(count_s)
        else:
            warn(warnings, base_line + off, f"Networking: unknown label {label!r}")
    if ethernet:
        data["ethernet"] = ethernet
    return data


_SERIAL_LABELS = [
    ("CAN", "can", True),
    ("RS-485", "rs485", True),
    ("RS-232", "rs232", True),
    ("LIN", "lin", True),
]


def parse_serial(bullets, base_line, warnings):
    return _parse_count_section(bullets, base_line, warnings, "Serial", _SERIAL_LABELS)


_USB_CONNECTORS = {"Type-A", "Type-B", "Type-C", "Mini-B", "Micro-B", "Header"}
_USB_SPEEDS = {"1.1", "2.0", "3.0", "3.1", "3.2", "4"}
_USB_ROLE_TOKEN = {"host": "host", "device": "device", "OTG": "otg"}


def parse_usb(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if len(toks) < 3:
            warn(warnings, base_line + off, f"USB: too few tokens in {text!r}")
            continue
        connector, speed, role_tok = toks[0], toks[1], toks[2]
        if connector not in _USB_CONNECTORS:
            warn(warnings, base_line + off, f"USB: unknown connector {connector!r}")
            continue
        if speed not in _USB_SPEEDS:
            warn(warnings, base_line + off, f"USB: unknown speed {speed!r}")
            continue
        if role_tok not in _USB_ROLE_TOKEN:
            warn(warnings, base_line + off, f"USB: unknown role {role_tok!r}")
            continue
        item = {"connector": connector, "speed": speed, "role": _USB_ROLE_TOKEN[role_tok]}
        if len(toks) == 4:
            m = re.fullmatch(r"x(\d+)", toks[3])
            if not m:
                warn(warnings, base_line + off, f"USB: expected x<N>, got {toks[3]!r}")
                continue
            item["ports"] = int(m.group(1))
        elif len(toks) > 4:
            warn(warnings, base_line + off, f"USB: extra tokens in {text!r}")
            continue
        items.append(item)
    return items


def parse_usb_bridge(bullets, base_line, warnings):
    items = []
    for text, off in bullets:
        toks = text.split()
        if len(toks) < 2:
            warn(warnings, base_line + off, f"USB UART/JTAG: too few tokens in {text!r}")
            continue
        connector, fns_tok = toks[0], toks[1]
        if connector not in _USB_CONNECTORS:
            warn(warnings, base_line + off, f"USB UART/JTAG: unknown connector {connector!r}")
            continue
        fns = [f.lower() for f in fns_tok.split("/")]
        if not all(f in ("jtag", "uart", "i2c") for f in fns):
            warn(warnings, base_line + off, f"USB UART/JTAG: unknown functions {fns_tok!r}")
            continue
        item = {"connector": connector, "functions": fns}
        if len(toks) == 3:
            m = re.fullmatch(r"x(\d+)", toks[2])
            if not m:
                warn(warnings, base_line + off, f"USB UART/JTAG: expected x<N>, got {toks[2]!r}")
                continue
            item["ports"] = int(m.group(1))
        elif len(toks) > 3:
            warn(warnings, base_line + off, f"USB UART/JTAG: extra tokens in {text!r}")
            continue
        items.append(item)
    return items


_FMC_TYPE_FROM_LABEL = {"HPC": "hpc", "LPC": "lpc", "FMC+": "fmcp"}
_EXPANSION_COUNT_LABELS = [
    ("Pmod", "pmod", True),
    ("Arduino", "arduino", True),
    ("Raspberry Pi", "raspberry_pi", True),
    ("Click", "click", True),
    ("SYZYGY", "syzygy", True),
    ("SYZYGY TRX", "syzygy_trx", True),
    ("RFMC", "rfmc", True),
    ("GPIO Header", "gpio_header", True),
    ("XADC Header", "xadc_header", True),
]
_EXPANSION_LABELS_BY_TEXT = {label: (key, _) for label, key, _ in _EXPANSION_COUNT_LABELS}

FMC_BULLET_RE = re.compile(
    r'^(?:FMC (HPC|LPC)|(FMC\+)) '
    r'"([^"]+)"'
    r'(?: VADJ (\d+(?:\.\d+)?)(?:-(\d+(?:\.\d+)?))?V)?'
    r'$'
)


def parse_expansion(bullets, base_line, warnings):
    data = {}
    fmc_slots = []
    for text, off in bullets:
        # FMC slot bullets
        m = FMC_BULLET_RE.match(text)
        if m:
            type_label = m.group(1) or m.group(2)
            slot_data = {
                "slot": m.group(3),
                "type": _FMC_TYPE_FROM_LABEL[type_label],
            }
            if m.group(4):
                vmin = parse_number(m.group(4))
                vmax = parse_number(m.group(5)) if m.group(5) else vmin
                slot_data["vadj_min"] = vmin
                slot_data["vadj_max"] = vmax
            fmc_slots.append(slot_data)
            continue
        # SYZYGY TRX must match before SYZYGY (longest first); regex handles this.
        m2 = re.match(r"^(SYZYGY TRX|Raspberry Pi|GPIO Header|XADC Header|Pmod|Arduino|Click|SYZYGY|RFMC) x(\d+)$", text)
        if m2 and m2.group(1) in _EXPANSION_LABELS_BY_TEXT:
            key, _ = _EXPANSION_LABELS_BY_TEXT[m2.group(1)]
            data[key] = int(m2.group(2))
            continue
        warn(warnings, base_line + off, f"Expansion: unrecognized {text!r}")
    if fmc_slots:
        data["fmc"] = fmc_slots
    return data


_STORAGE_LABELS = [
    ("SATA", "sata", True),
    ("SD", "sd", True),
    ("microSD", "microsd", True),
]


def parse_storage(bullets, base_line, warnings):
    return _parse_count_section(bullets, base_line, warnings, "Storage", _STORAGE_LABELS)


_USER_IO_LABELS = [
    ("LEDs", "leds", True),
    ("RGB LEDs", "rgb_leds", True),
    ("Pushbuttons", "pushbuttons", True),
    ("DIP switches", "dip_switches", True),
    ("7-segment displays", "seven_segment", True),
    ("Rotary encoders", "rotary_encoders", True),
]


def parse_user_io(bullets, base_line, warnings):
    return _parse_count_section(bullets, base_line, warnings, "User I/O", _USER_IO_LABELS)


def parse_wireless(bullets, base_line, warnings):
    data = {}
    for text, off in bullets:
        if text == "WiFi":
            data["wifi"] = True
        elif text == "Bluetooth":
            data["bluetooth"] = True
        else:
            warn(warnings, base_line + off, f"Wireless: unrecognized {text!r}")
    return data


_FEATURE_BULLETS = {
    "Power monitoring": "power_monitoring",
    "Programmable VADJ": "programmable_vadj",
    "Battery-backed RTC": "battery_backed_rtc",
    "Secure element": "secure_element",
    "Tamper detection": "tamper_detection",
}


def parse_features(bullets, base_line, warnings):
    data = {}
    for text, off in bullets:
        key = _FEATURE_BULLETS.get(text)
        if key is None:
            warn(warnings, base_line + off, f"Features: unrecognized {text!r}")
            continue
        data[key] = True
    return data


SECTION_PARSERS = {
    "Memory": parse_memory,
    "Flash": parse_flash,
    "EEPROM": parse_eeprom,
    "Analog": parse_analog,
    "Sensors": parse_sensors,
    "Audio": parse_audio,
    "Clocking": parse_clocking,
    "PCIe": parse_pcie,
    "M.2": parse_m2,
    "High-speed I/O": parse_high_speed_io,
    "Video": parse_video,
    "Display": parse_display,
    "Networking": parse_networking,
    "Serial": parse_serial,
    "USB": parse_usb,
    "USB UART/JTAG": parse_usb_bridge,
    "Expansion": parse_expansion,
    "Storage": parse_storage,
    "User I/O": parse_user_io,
    "Wireless": parse_wireless,
    "Features": parse_features,
}


# ============================================================================
# Top-level parse
# ============================================================================

def parse(md_text, entity_type):
    result = ParseResult(data={})
    fm, body, body_start = split_front_matter(md_text)
    validate_front_matter(fm, entity_type, result.warnings)

    # Copy front-matter into result.data
    for key, val in fm.items():
        result.data[key] = val

    sections = split_sections(body, body_start)
    for heading, content, line in sections:
        bullets = extract_bullets(content)

        if heading == "Notes":
            result.notes = content.strip("\n") or None
            continue
        if heading == "Extras":
            result.extras = [t for t, _ in bullets]
            continue
        if heading == "Includes":
            if entity_type == "kit":
                result.data["extras"] = [t for t, _ in bullets]
            else:
                result.warnings.append(
                    f"line {line}: ## Includes only valid for kit entities"
                )
            continue

        parser = SECTION_PARSERS.get(heading)
        if parser is None:
            result.unknown_sections.append(heading)
            result.warnings.append(f"line {line}: unknown section {heading!r}")
            continue

        json_key = SECTION_HEADING_TO_KEY[heading]
        section_data = parser(bullets, line + 1, result.warnings)
        if section_data:
            result.data[json_key] = section_data

    return result


def parse_file(path):
    """Parse a .md file, inferring entity type from its path."""
    path = Path(path)
    entity_type = None
    for part in path.parts:
        if part in PATH_TO_ENTITY_TYPE:
            entity_type = PATH_TO_ENTITY_TYPE[part]
            break
    if entity_type is None:
        raise ValueError(f"can't infer entity type from path: {path}")
    return parse(path.read_text(encoding="utf-8"), entity_type)


# ============================================================================
# CLI
# ============================================================================

def cli_one(path):
    result = parse_file(path)
    print(json.dumps(result.data, indent=2))
    for w in result.warnings:
        print(f"  warning: {w}", file=sys.stderr)
    if result.unknown_sections:
        print(f"  unknown sections: {result.unknown_sections}", file=sys.stderr)
    if result.extras:
        print(f"  extras ({len(result.extras)}): {result.extras}", file=sys.stderr)


def cli_check(root):
    n = 0
    warned = 0
    errored = 0
    for md_path in sorted(Path(root).rglob("*.md")):
        # Skip anything that doesn't live under one of the entity folders
        if not any(p in PATH_TO_ENTITY_TYPE for p in md_path.parts):
            continue
        n += 1
        try:
            result = parse_file(md_path)
        except Exception as e:
            errored += 1
            print(f"{md_path}: ERROR {e}", file=sys.stderr)
            continue
        if result.warnings:
            warned += 1
            for w in result.warnings:
                print(f"{md_path}: {w}", file=sys.stderr)
    print(f"checked {n} files; {warned} with warnings, {errored} errored")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", help="Path to .md file or directory")
    ap.add_argument("--check", action="store_true",
                    help="Recursively parse a directory and report issues only")
    args = ap.parse_args()

    target = Path(args.target)
    if args.check:
        if not target.is_dir():
            ap.error("--check requires a directory")
        cli_check(target)
    else:
        cli_one(target)


if __name__ == "__main__":
    main()
