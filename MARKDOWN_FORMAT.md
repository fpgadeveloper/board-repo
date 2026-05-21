# Canonical markdown format

Reference spec for the per-entity `.md` files in this repo. Defines exactly what the strict parser (`scripts/json_from_md.py`, in this repo) accepts. Read alongside `schema.json` — schema says what data is legal, this doc says what string form represents it.

Audiences:
- **Contributors** editing `.md` files on GitHub — write canonical bullets, the validator will be happy. If you don't know the canonical form, write what makes sense to you; the maintainer's PR script will canonicalize it.
- **Claude** (the assistant) — when canonicalizing PRs or generating markdown from a submit-form paste, this is the spec to satisfy. Together with `schema.json`, it tells you what's legal.
- **The parser** — derived from this doc. If parser and doc drift, this doc is the source of truth; fix the parser.

Status: draft. Working examples for all entity types live in `REWORK.md` in the website repo.

## File anatomy

```markdown
---
<YAML front-matter — identity fields>
---

## <Section Name>
- <canonical bullet>
- <canonical bullet>

## <Section Name>
- <canonical bullet>

## Extras
- <free-form bullet — unmodeled feature>

## Notes
<free-form prose, paragraphs, tables, etc.>
```

- Front-matter is required. It holds identity-class fields (MPN, name, status, URL, vendor, price, and entity-specific bits like `device` / `composition` / `connector_type`).
- Feature sections come next, in any order. Section heading wording is fixed per the table below; only sections with at least one bullet are present.
- `## Extras` and `## Notes` are universal optional sections at the end. Extras holds unmodeled features; Notes holds prose (boot-mode tables, gotchas, etc.).

## Bullet syntax conventions

- **Succinct, space-separated tokens** — no commas, no extra whitespace. `DDR4 2GB 64-bit`, not `DDR4, 2 GB, 64 bit`.
- **No space between number and unit** — `2GB`, `100MHz`, `1GbE`, `64-bit`. Exception: VADJ ranges write `1.5-1.8V` (hyphen separator, V at end).
- **Counts use an `x<N>` suffix — follow each section's grammar exactly.** Where a grammar shows `xN` (`Pmod xN`, `LEDs xN`, `HDMI Out xN`, `SFP+ xN`, …) the suffix is **required, including a count of one** — write `Pmod x1`, never a bare `Pmod`. Omit it *only* where a grammar shows `[xN]` in brackets (USB, USB UART/JTAG, and High-speed I/O), for a single port / connector. Boolean bullets that carry no count token at all (`Speaker`, `Programmable`, `WiFi`) never take one.
- **Token order is fixed per section**, defined below. Parser is positional within each section's grammar.
- **Optional tokens are appended in fixed order** — for example memory is `<type> <size> [<width>-bit] [ECC] [<form_factor>]`. Skip any optional token by leaving it out.

## Front-matter

YAML, inline-mapping form for compactness. Required fields per entity type:

| Field | standalone | som | carrier | kit | fmc_card |
|---|---|---|---|---|---|
| `mpn` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `name` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `status` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `url` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vendor` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `price` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `device` | ✓ | ✓ | — | — | — |
| `composition` | — | — | — | ✓ | — |
| `connector_type` | — | — | — | — | ✓ |
| `vadj_min` / `vadj_max` | — | — | — | — | optional |

Field shapes:

- `status` — one of `active`, `nrnd`, `eol`, `discontinued`.
- `price` — `{ value: <number>, currency: <ISO-4217> }` or `null` (entity not sold standalone).
- `device` — `{ part: <full-part-number>, vendor: <silicon-vendor-key> }`. Part must be a complete decoder-valid orderable part.
- `composition` (kits only) — `{ som: <som-mpn>, carrier: <carrier-mpn> }`.
- `connector_type` (FMC cards) — `lpc` | `hpc` | `fmcp`.

Example block:

```yaml
---
mpn: KCU105
name: KCU105
status: active
url: https://www.amd.com/en/products/.../kcu105.html
vendor: amd-xilinx
price: { value: 6495, currency: USD }
device: { part: XCKU040-2FFVA1156E, vendor: amd-xilinx }
---
```

## Sections

Each section's heading wording is fixed. Sections appear only when they have ≥1 bullet. Bullets within a section may appear in any order — the parser doesn't depend on bullet order. Token order *within* a bullet is fixed.

### `## Memory`

Schema: `memory[]` (array of `memory_interface`).

Grammar: `<type> <size> [<width>-bit] [ECC] [<form_factor>]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | Enum literal: `SDRAM`, `DDR3`, `DDR4`, `LPDDR`, `LPDDR4`, `HBM2`, `QDR-II+`, `RLD3`, `HyperRAM`, `PSRAM`, etc. |
| `size` | `size_mb` | Integer + `GB` (when `size_mb` is a multiple of 1024) or `MB` |
| `width` | `width_bits` | `<N>-bit` |
| `ECC` | `ecc: true` | Literal `ECC` |
| `form_factor` | `form_factor` | Uppercased enum value: `SODIMM`, `DIMM`, `UDIMM`, `RDIMM`, `LRDIMM`. Omit when `component` (default). |

Examples:
- `DDR4 2GB 64-bit`
- `DDR4 8GB 72-bit ECC`
- `DDR4 16GB 64-bit SODIMM`
- `HBM2 8GB`

### `## SRAM`

Schema: `sram[]` (array of `sram_interface`). Discrete static / non-volatile RAM chips — distinct from the DRAM banks in `## Memory`. HyperRAM and PSRAM are pseudo-static DRAM and belong in `## Memory`, not here.

Grammar: `<type> <size> [<width>-bit] [<interface>]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | Enum literal: `SRAM`, `SSRAM`, `MRAM`, `FRAM`, `nvSRAM` |
| `size` | `size_kb` | Integer + `KB`, `MB`, or `GB` |
| `width` | `width_bits` | `<N>-bit` |
| `interface` | `interface` | Literal `SPI` or `QSPI`; omit when `parallel` (default) |

Examples:
- `SRAM 512KB 8-bit`
- `SSRAM 2MB 16-bit`
- `MRAM 4MB`
- `SRAM 512KB SPI`

### `## Flash`

Schema: `flash[]` (array of `flash_interface`).

Grammar: `<type> <size> [<width>-bit]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | Enum: `QSPI`, `OSPI`, `SPI`, `BPI`, `eMMC`, `NAND` |
| `size` | `size_mb` | `<N>GB` or `<N>MB` (rounding rule as for Memory) |
| `width` | `width_bits` | `<N>-bit` |

Examples:
- `QSPI 32MB`
- `BPI 64MB 16-bit`
- `eMMC 16GB`

### `## EEPROM`

Schema: `eeprom[]` (array of `eeprom_chip`).

Grammar: `<purposes> [<interface>] [<size>] [<part>]`

| Token | Schema field | Form |
|---|---|---|
| `purposes` | `purpose[]` | Short codes joined with `+`: `MAC` (mac_address), `UID` (unique_id), `ID` (board_id), `data` (user_data). Example: `MAC+UID`. |
| `interface` | `interface` | Enum literal: `I2C`, `SPI`, `1-Wire` |
| `size` | `size_kbits` | `<N>Kbit` |
| `part` | `part` | Manufacturer part number, last token |

Examples:
- `MAC+UID I2C 8Kbit AT24C512`
- `ID I2C 4Kbit`
- `data SPI`

### `## Analog`

Schema: `analog[]` (array of `analog_chip`).

Grammar: `<role> [<part>] [<channels>ch] [<bits>-bit] [<rate>MSPS | <fmin>-<fmax>MHz]`

| Token | Schema field | Form |
|---|---|---|
| `role` | `role` | Display label: `ADC`, `DAC`, `RF`, `AFE` |
| `part` | `part` | Manufacturer part number |
| `channels` | `channels` | `<N>ch` |
| `bits` | `resolution_bits` | `<N>-bit` (ADC/DAC) |
| `rate` | `sample_rate_msps` | `<N>MSPS` (ADC/DAC) |
| `freq range` | `frequency_min_mhz` / `frequency_max_mhz` | `<min>-<max>MHz` (RF / AFE) |

Examples:
- `ADC LTC2387 1ch 18-bit 15MSPS`
- `DAC AD9162 1ch 16-bit 6000MSPS`
- `RF AD9361 2ch 70-6000MHz`
- `AFE` (no extras known)

### `## Sensors`

Schema: `sensors[]` (array of `sensor`).

Grammar: `<type> [<part>]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | Display label: `IMU`, `Accelerometer`, `Gyroscope`, `Magnetometer`, `Temperature`, `Pressure`, `Humidity`, `Light`, `Proximity`, `Microphone`, `Camera` |
| `part` | `part` | Manufacturer part number |

Examples:
- `IMU MPU-9250`
- `Temperature TMP102`
- `Microphone`

### `## Audio`

Schema: `audio` (singleton object).

Bullets — one per non-default attribute:

| Bullet | Schema field |
|---|---|
| `Codec <part>` | `codec` |
| `Line in xN` | `line_in` |
| `Line out xN` | `line_out` |
| `Headphone xN` | `headphone_jack` |
| `Microphone xN` | `microphone` |
| `Speaker` | `speaker: true` |

Examples:
- `Codec SSM2603`
- `Line in x1`
- `Line out x1`
- `Headphone x1`

### `## Clocking`

Schema: `clocking` (singleton object).

| Bullet | Schema field |
|---|---|
| `Programmable` | `programmable: true` |
| `SMA clock in xN` | `sma_clock_in` |
| `SMA clock out xN` | `sma_clock_out` |
| `GPSDO` | `gps_disciplined: true` |

### `## PCIe`

Schema: `pcie[]` (array of `pcie_interface`).

Grammar: `<type> [Gen<N>] [x<lanes>] [+mSATA]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | Enum literal: `Edge`, `Slot`, `PCIe/104`, `iPass`, `MCIO`, `MiniPCIe-Half`, `MiniPCIe-Full` |
| `Gen<N>` | `gen` | `Gen` + integer |
| `x<lanes>` | `lanes` | `x` + integer |
| `+mSATA` | `msata_capable: true` | Literal `+mSATA`, MiniPCIe only |

Examples:
- `Edge Gen3 x8`
- `MiniPCIe-Full Gen2 x1 +mSATA`
- `MCIO Gen4 x4`
- `Slot Gen2 x1`

### `## M.2`

Schema: `m2[]` (array of `m2_interface`).

Grammar: `<key> [(FF)] [<interfaces>] [Gen<N>] [x<lanes>] [<length>]`

| Token | Schema field | Form |
|---|---|---|
| `key` | `key` | Enum: `M-key`, `E-key`, `B-key`, `B+M-key` |
| `(FF)` | `direction: form-factor` | Literal `(FF)`; omit for `socket` (default) |
| `interfaces` | `interfaces[]` | Only when not default for the key. Joined with `+`. Defaults: M-key/B+M-key → PCIe, E-key → PCIe+USB, B-key → USB. |
| `Gen<N>` | `gen` | |
| `x<lanes>` | `lanes` | |
| `length` | `length` | M.2 length literal: `2230`, `2242`, `2260`, `2280`, `22110` |

Examples:
- `M-key Gen4 x4 2280` (typical NVMe socket)
- `E-key 2230` (WiFi/BT default interfaces, length)
- `M-key SATA 2242` (ZCU-style SATA-only M.2)
- `M-key (FF) Gen2 x4 22110` (LiteFury — board IS an M.2 module)

### `## High-speed I/O`

Schema: `high_speed_io[]` (array of `transceiver_connector`). Connectors that
break out the FPGA's serial transceiver lanes outside the PCIe protocol wrapper.
One bullet per connector form.

Grammar: `<form> [xN] [<lanes>-lane] [<type>] [<rate>Gbps]`

| Token | Schema field | Form |
|---|---|---|
| `form` | `form` | Enum literal: `SMA`, `FireFly`, `SlimSAS`, `BullsEye`, `MXP`, `Mini-DP`, `Z-Ray` |
| `xN` | `count` | `x` + integer; omit when 1 |
| `lanes` | `lanes` | `<N>-lane` — total transceiver lanes across all `xN` connectors |
| `type` | `transceiver` | Transceiver-type token: `GTP`, `GTX`, `GTH`, `GTY`, `GTYP`, `GTM`, `GTF`, `PS-GTR`, or a vendor equivalent |
| `rate` | `max_rate_gbps` | `<N>Gbps` — maximum per-lane line rate |

Examples:
- `SMA x4 4-lane GTH`
- `FireFly x1 4-lane GTY 28.21Gbps`
- `BullsEye 8-lane GTM 112Gbps`
- `Mini-DP x2`

### `## Video`

Schema: `video` (object of counts). One bullet per non-zero key:

| Bullet | Schema field |
|---|---|
| `HDMI In xN` / `HDMI Out xN` | `hdmi_in` / `hdmi_out` |
| `DisplayPort xN` | `displayport` |
| `SDI In xN` / `SDI Out xN` | `sdi_in` / `sdi_out` |
| `AES3 In xN` / `AES3 Out xN` | `aes_in` / `aes_out` |
| `MIPI DSI xN` / `MIPI CSI xN` | `mipi_dsi` / `mipi_csi` |
| `VGA Out xN` | `vga_out` |

### `## Display`

Schema: `display` (singleton object). One bullet per non-default attribute:

| Bullet | Schema field |
|---|---|
| `Character LCD <rows>x<cols>` | `character_lcd` (e.g. `2x16`) |
| `OLED <width>x<height>` | `oled` (e.g. `128x64`) |

### `## Networking`

Schema: `networking` (mixed — `ethernet[]` array plus per-cage counts).

Ethernet bullets — one per `(speed, ports)` pair: `<speed-label> x<ports> [<endpoint>]`

`<endpoint>` is an optional trailing token marking which part of the Ethernet
chain the entity carries — omit it for a complete port:

| Token | `endpoint` | Meaning |
|---|---|---|
| *(omitted)* | `phy+rj45` | Complete port — PHY + RJ45 jack (standalone boards) |
| `PHY-only` | `phy` | PHY/MAC exposed, no jack — the jack is on the carrier (SoMs) |
| `RJ45-only` | `rj45` | RJ45 jack + magnetics, PHY supplied by a mated SoM (some carriers) |

Examples: `1GbE x1`, `1GbE x2 PHY-only`, `2.5GbE x1 RJ45-only`.

| Speed | Label |
|---|---|
| 10 | `10Mbps` |
| 100 | `100Mbps` |
| 1000 | `1GbE` |
| 2500 | `2.5GbE` |
| 5000 | `5GbE` |
| 10000 | `10GbE` |
| 25000 | `25GbE` |
| 40000 | `40GbE` |
| 100000 | `100GbE` |

Cage bullets — one per non-zero cage field:

| Bullet | Schema field |
|---|---|
| `SFP xN` | `sfp` |
| `SFP+ xN` | `sfp_plus` |
| `SFP28 xN` / `SFP56 xN` / `SFP-DD xN` | `sfp28` / `sfp56` / `sfp_dd` |
| `QSFP xN` | `qsfp` |
| `QSFP+ xN` | `qsfp_plus` |
| `QSFP28 xN` / `QSFP56 xN` / `QSFP-DD xN` / `QSFP-DD800 xN` | `qsfp28` / `qsfp56` / `qsfp_dd` / `qsfp_dd800` |
| `OSFP xN` / `OSFP-XD xN` | `osfp` / `osfp_xd` |
| `CFP xN` / `CFP2 xN` / `CFP4 xN` / `CFP8 xN` | `cfp` / `cfp2` / `cfp4` / `cfp8` |

### `## Serial`

Schema: `serial` (object of counts).

| Bullet | Schema field |
|---|---|
| `CAN xN` | `can` |
| `RS-485 xN` | `rs485` |
| `RS-232 xN` | `rs232` |
| `LIN xN` | `lin` |

### `## USB`

Schema: `usb[]` (array of `usb_interface`).

Grammar: `<connector> <speed> <role> [xN]`

| Token | Schema field | Form |
|---|---|---|
| `connector` | `connector` / `endpoint` | Enum: `Type-A`, `Type-B`, `Type-C`, `Mini-B`, `Micro-B`, `Header` — or the literal `PHY` for a USB PHY / ULPI transceiver with no receptacle of its own (the receptacle sits on a mated carrier — typical SoM). `PHY` sets `endpoint: phy` and omits `connector`; any other value sets `connector` and leaves `endpoint` at its default (`connector`). |
| `speed` | `speed` | Enum: `1.1`, `2.0`, `3.0`, `3.1`, `3.2`, `4` |
| `role` | `role` | `host`, `device`, `OTG` (display form of `otg`) |
| `xN` | `ports` | Omit when 1 |

Examples:
- `Type-A 3.0 host x4`
- `Type-C 3.2 OTG`
- `Micro-B 2.0 device`
- `PHY 2.0 OTG` (SoM-side USB PHY — receptacle on the carrier)

### `## USB UART/JTAG`

Schema: `usb_bridge[]` (array of `usb_bridge_interface`).

Grammar: `<connector> <functions> [xN]`

| Token | Schema field | Form |
|---|---|---|
| `connector` | `connector` | Same set as USB |
| `functions` | `functions[]` | Joined with `/`, uppercased: `JTAG`, `UART`, `I2C`, e.g. `JTAG/UART`, `JTAG/I2C` |
| `xN` | `ports` | Omit when 1 |

Examples:
- `Micro-B JTAG/UART`
- `Micro-B JTAG`
- `Micro-B UART`

### `## Expansion`

Schema: `expansion` (mixed — `fmc[]` array plus per-connector counts).

FMC slot bullets — one per slot: `FMC <type> "<slot-name>" [VADJ <range>]`

| Token | Schema field | Form |
|---|---|---|
| `type` | `type` | `HPC`, `LPC`, `FMC+` (display form of `fmcp`) |
| `slot-name` | `slot` | Slot name in double quotes |
| `VADJ <range>` | `vadj_min` / `vadj_max` | `VADJ <min>-<max>V`, or `VADJ <v>V` when min == max |

Examples:
- `FMC HPC "HPC0" VADJ 1.5-1.8V`
- `FMC LPC "LPC1" VADJ 1.8V`
- `FMC+ "J3"` (no VADJ data)

Other expansion bullets — one per non-zero key:

| Bullet | Schema field |
|---|---|
| `Pmod xN` | `pmod` |
| `Arduino xN` | `arduino` |
| `Raspberry Pi xN` | `raspberry_pi` |
| `Click xN` | `click` |
| `SYZYGY xN` / `SYZYGY TRX xN` | `syzygy` / `syzygy_trx` |
| `RFMC xN` | `rfmc` |
| `GPIO Header xN` | `gpio_header` |
| `XADC Header xN` | `xadc_header` |
| `HSMC xN` | `hsmc` |
| `CRUVI HS xN` / `CRUVI LS xN` | `cruvi_hs` / `cruvi_ls` |
| `Grove xN` | `grove` |
| `96Boards LS xN` / `96Boards HS xN` | `boards96_ls` / `boards96_hs` |

### `## Storage`

Schema: `storage` (object of counts).

| Bullet | Schema field |
|---|---|
| `SATA xN` | `sata` |
| `SD xN` | `sd` |
| `microSD xN` | `microsd` |

### `## User I/O`

Schema: `user_io` (object of counts).

| Bullet | Schema field |
|---|---|
| `LEDs xN` | `leds` |
| `RGB LEDs xN` | `rgb_leds` |
| `Pushbuttons xN` | `pushbuttons` |
| `DIP switches xN` | `dip_switches` |
| `7-segment displays xN` | `seven_segment` |
| `Rotary encoders xN` | `rotary_encoders` |

### `## Wireless`

Schema: `wireless` (booleans).

| Bullet | Schema field |
|---|---|
| `WiFi` | `wifi: true` |
| `Bluetooth` | `bluetooth: true` |

### `## Features`

Schema: `features` (booleans). Labels mirror schema `title`:

| Bullet | Schema field |
|---|---|
| `Power monitoring` | `power_monitoring` |
| `Programmable VADJ` | `programmable_vadj` |
| `RTC` | `rtc` |
| `Battery-backed RTC` | `battery_backed_rtc` |
| `Secure element` | `secure_element` |
| `Tamper detection` | `tamper_detection` |

## Universal sections

### `## Includes` (kits only)

Schema: `extras[]` (array of free-form strings). Items shipped in the box beyond the SoM + carrier — cables, PSUs, antennas, etc. Maps to JSON field `extras` (heading differs from JSON field name to avoid clashing with the universal `## Extras` section below).

```markdown
## Includes
- USB-A to micro-USB cable
- 12V power supply
- Antenna kit
```

### `## Extras`

Unmodeled features — anything the schema doesn't cover yet but is worth preserving in source form. The parser **does not** convert these to JSON; they survive only in the markdown until the schema is extended.

```markdown
## Extras
- Onboard IPMI BMC for remote management
- Crypto offload accelerator (L2 inline)
- Custom debug header (vendor-proprietary)
```

When the schema later adds a field for one of these features, the maintainer sweeps Extras lines into their proper section.

### `## Notes`

Free-form prose — boot-mode tables, default jumper positions, gotchas, errata. Markdown is rendered into HTML on the board detail page (same plumbing as today's `notes/<vendor>/<mpn>.md`).

```markdown
## Notes

Boot-mode DIP switches:

| Mode | SW1.1 | SW1.2 | SW1.3 |
|---|---|---|---|
| JTAG | ON  | ON  | ON  |
| QSPI | OFF | OFF | OFF |

The default jumper config ships with VADJ = 1.8V.
```

## Parser rules

The parser (`scripts/json_from_md.py`) is strict but tolerant of unmodeled data:

1. **Front-matter** must parse as YAML and match the entity-type field set above. Failure to parse is a hard error.
2. **Section headings** are matched exactly (case-sensitive, whitespace-normalized). Unknown headings (e.g. `## Power`) leave the section preserved in markdown but unparsed — they don't error.
3. **Bullets in known sections** are matched against the grammar above. Recognized bullets become JSON. Unrecognized bullets emit a warning — the parser itself never raises on them; they remain in the markdown for the next pass to handle.
4. **`## Extras` and `## Notes`** are never parsed into JSON. Extras bullets survive verbatim; Notes is rendered to HTML at build time.
5. **Schema validation** runs on the produced JSON. Schema failure = hard error.

"Warns, doesn't raise" is *parser* behaviour. CI policy is stricter — `.github/workflows/validate.yml` **fails** a PR when:

- front-matter fails to parse or is missing a required identity field;
- the produced JSON fails schema validation;
- an MPN collides across the entity folders;
- a bullet in a **known section** fails to match the canonical grammar.

An **unknown section heading** (e.g. `## Power`) does *not* fail CI — it's reported as an annotation and the section is preserved in the `.md`. `## Extras` content never fails anything. So contributors don't have to nail canonical form on the first push: near-miss bullets show red until the maintainer's PR-processing script canonicalizes them, but unmodeled features parked in `## Extras` (or a whole unknown section) sail through.

## Round-trip and stability

- **Cutover** (one-shot): `JSON → MD → JSON` produces zero diff across the existing corpus. Achievable because the source JSON has no Extras yet.
- **Ongoing** (per PR): `MD → JSON` is idempotent. Running the parser twice on the same `.md` produces identical JSON; Extras and unparsed bullets are preserved across edits.
- **After cutover**, JSON is never regenerated from MD with intent to overwrite — JSON is a build artifact in the website repo's `data/` tree, gitignored.

## Open spec questions

- VADJ range when `vadj_min == vadj_max` — currently spec'd as a single value (`VADJ 1.8V`). Consider always-range form (`VADJ 1.8-1.8V`) for parser uniformity.
- Sensor type display labels — schema enum is lowercase, but the labels here use title-case (`Temperature`, `Microphone`). Confirm vs the live UI before committing.
- Whether to allow comments (`<!-- ... -->`) anywhere in the file. Probably yes — they survive parsing trivially.
- Whether to require a blank line between sections (cosmetic, parser-safe either way).
