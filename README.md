# FPGA Board Repository

This repository contains the community-maintained database of FPGA development boards, system-on-modules, carriers, kits, and FMC mezzanine cards used by [FPGA Board Repository](https://boards.fpgadeveloper.com). Contributions are welcome — if you know of an entity that's missing, you can add it here.

## Files

| Path | Description |
|------|-------------|
| `boards/` | Standalone FPGA boards (the FPGA, memory, peripherals, and I/O all on one PCB). One file per board, organized by vendor (e.g. `boards/amd-xilinx/ZCU102.json`). |
| `soms/` | System-on-modules — small daughter boards carrying the FPGA, memory, and flash, designed to plug into a carrier (e.g. `soms/amd-xilinx/SM-K26-XCL2GC.json`). |
| `carriers/` | Carrier boards that host a SoM and supply power + I/O (e.g. `carriers/amd-xilinx/KR260-Carrier.json`). |
| `kits/` | Pre-assembled SoM + carrier bundles sold as a single SKU. Each kit references its components by MPN (e.g. `kits/amd-xilinx/SK-KR260-G.json`). |
| `fmc-cards/` | FPGA Mezzanine Cards (VITA 57: LPC / HPC / FMC+) that plug into FMC sites on a host (e.g. `fmc-cards/opsero/OP120.json`). |
| `relationships/` | Compatibility relationships between entities (which FMC cards mate with which hosts; which SoMs fit which carriers). See [Compatibility Relationships](#compatibility-relationships) below. |
| `parts/` | Part-number decoder files, one per FPGA family (e.g. `parts/amd-xilinx/Spartan-7.json`). See [Part Number Decoders](#part-number-decoders) below. |
| `attributes/` | Per-vendor device attributes that extend the board detail page (ML support, resource counts, transceivers, ...). See [`attributes/README.md`](attributes/README.md). |
| `notes/` | Per-entity markdown notes (boot-mode tables, default jumper positions, gotchas). See [`notes/README.md`](notes/README.md). |
| `vendors.json` | Centralized registry of board vendors and silicon vendors. |
| `schema.json` | JSON Schema (Draft 2020-12) that validates entities and relationships. |

## How to Contribute

### Option 1: Submit via the Website

The easiest way to add a board is through the **Submit** page on the website:

**[boards.fpgadeveloper.com/submit.html](https://boards.fpgadeveloper.com/submit.html)**

Fill in the form and your submission will be reviewed and added to the database.

The website form currently covers standalone boards. For SoMs, carriers, kits, FMC cards, relationships, notes, and attributes, use a pull request (Option 2).

### Option 2: Submit a Pull Request

Fork the repo, add or edit the relevant JSON / markdown file(s), and open a PR. The format reference for each entity type is below.

1. **Fork** this repository.
2. **Create or edit** the relevant file under the matching entity folder (see [Entity Types](#entity-types) below).
3. **Validate** your changes against the schema (see [Validation](#validation) below).
4. **Open a pull request** with a brief description.

## Entity Types

What follows is a contributor-friendly summary of each entity's JSON shape. `schema.json` is the canonical source — refer to it for the full set of optional fields and constraints.

### Boards

A **standalone board** is a single PCB carrying the FPGA, memory, flash, and I/O. It does not require a separate carrier or daughter card to run.

File: `boards/<vendor>/<mpn>.json` (filename matches the `mpn` field).

Required fields:

| Field | Type | Description |
|-------|------|-------------|
| `mpn` | string | Manufacturer part number — e.g. `"ZCU102"`, `"DK-DEV-AGI027-RA-B"`, `"DK_START_GW1NR-LV9LQ144PC6I5"`. Must be unique across all entities. Some older entries predate this convention and use a short product name; new entries should use the vendor's MPN. |
| `name` | string | Human-readable display name (e.g. `"Kintex UltraScale+ KCU105"`). |
| `status` | string | `"active"`, `"nrnd"` (not recommended for new designs), `"eol"` (end-of-life), or `"discontinued"`. |
| `url` | string | Product page URL. |
| `vendor` | string | Board vendor key (must match a key in `vendors.json` `board_vendors`). |
| `price` | object \| null | `{ "value": 129.00, "currency": "USD" }`, or `null` for boards not sold separately. |
| `device` | object | FPGA/SoC info: `{ "part": "<full orderable part number>", "vendor": "<silicon-vendor-key>" }`. |

Optional sections (only include what applies): `memory`, `flash`, `pcie`, `video`, `networking`, `usb`, `usb_bridge`, `expansion` (FMC sites, Pmod, Arduino, mikroBUS, ...), `storage`, `wireless`.

`usb` covers USB ports accessible to the FPGA design (fabric or hard IP); `usb_bridge` covers USB-to-UART/JTAG ports for board configuration and serial console (e.g. FT2232, CP2102). They're kept separate because bridge ports never reach the FPGA fabric.

#### Minimal example

`boards/digilent/Arty-A7.json`:

```json
{
  "mpn": "Arty-A7",
  "name": "Arty A7",
  "status": "active",
  "url": "https://digilent.com/shop/arty-a7/",
  "vendor": "digilent",
  "price": { "value": 129.00, "currency": "USD" },
  "device": { "part": "XC7A35T-1CPG236C", "vendor": "amd-xilinx" }
}
```

#### Example with interfaces

`boards/amd-xilinx/SP701.json`:

```json
{
  "mpn": "SP701",
  "name": "SP701",
  "status": "active",
  "url": "https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/sp701.html",
  "vendor": "amd-xilinx",
  "price": { "value": 836, "currency": "USD" },
  "device": { "part": "XC7S100-2FGGA676C", "vendor": "amd-xilinx" },
  "memory": [
    { "type": "DDR3L", "size_mb": 512, "width_bits": 16 }
  ],
  "video": { "hdmi_out": 1, "mipi_dsi": 1, "mipi_csi": 1 },
  "networking": {
    "ethernet": [{ "speed": 1000, "ports": 2 }]
  },
  "usb_bridge": [
    { "connector": "Micro-B", "functions": ["jtag", "uart"] }
  ],
  "expansion": {
    "fmc": [
      { "slot": "LPC", "type": "lpc", "vadj_min": 1.8, "vadj_max": 3.3 }
    ],
    "pmod": 6
  }
}
```

Each FMC site on the board is one entry in `expansion.fmc[]`. `slot` is the silkscreen name (e.g. `LPC`, `HPC0`, `FMCP1`) and is referenced by name from `fmc-mates` relationships. `type` is one of `lpc` / `hpc` / `fmcp`. FMC-card compatibility itself lives in [relationships](#compatibility-relationships) — the board file just says where the sites are.

### SoMs

A **system-on-module** is a small daughter board carrying the FPGA, memory, and flash. It plugs into a carrier or kit, which supplies power and the bulk of the I/O.

File: `soms/<vendor>/<mpn>.json`.

Required: `mpn`, `name`, `status`, `url`, `vendor`, `price`, `device`. Optional: `memory`, `flash`.

Most SoMs expose only `device` + `memory` + `flash` — the carrier provides everything else. The schema does also allow a few SoM-edge peripherals (`networking`, `usb`, `usb_bridge`, `expansion` (without `fmc` — FMC sites are carrier-owned), `storage`, `wireless`) for the rare SoMs that bring their own. The Avnet MicroZed is one example: it carries its own Ethernet, USB, and a Pmod. `pcie` and `video` are not allowed on SoMs — they only exist on the carrier side.

Example — `soms/amd-xilinx/SM-K26-XCL2GC.json`:

```json
{
  "mpn": "SM-K26-XCL2GC",
  "name": "Kria K26 SOM",
  "status": "active",
  "url": "https://www.amd.com/en/products/system-on-modules/kria/k26.html",
  "vendor": "amd-xilinx",
  "price": { "value": 350, "currency": "USD" },
  "device": { "part": "XCK26-2LSGVA1156C", "vendor": "amd-xilinx" },
  "memory": [{ "type": "DDR4", "size_mb": 4096, "width_bits": 64 }],
  "flash": [
    { "type": "QSPI", "size_mb": 64 },
    { "type": "eMMC", "size_mb": 16384 }
  ]
}
```

Which carriers a SoM fits on is recorded in [relationships](#compatibility-relationships) (`som-mates`).

### Carriers

A **carrier** hosts a SoM and exposes its I/O (Ethernet, USB, PCIe, FMC, Pmod, ...) plus power. It's the SoM's counterpart.

File: `carriers/<vendor>/<mpn>.json`.

Required: `mpn`, `name`, `status`, `url`, `vendor`, `price`. Optional: all the I/O sections from boards (`pcie`, `video`, `networking`, `usb`, `usb_bridge`, `expansion`, `storage`, `wireless`).

Use `"price": null` for carriers that aren't sold standalone (only inside a kit). For carriers like that, invent a stable MPN such as `<kit-mpn>-Carrier`.

Example — `carriers/amd-xilinx/KV260-Carrier.json`:

```json
{
  "mpn": "KV260-Carrier",
  "name": "Kria KV260 Vision Carrier",
  "status": "active",
  "url": "https://www.amd.com/en/products/system-on-modules/kria/k26/kv260-vision-starter-kit.html",
  "vendor": "amd-xilinx",
  "price": null,
  "video": { "hdmi_out": 1, "displayport": 1, "mipi_csi": 3 },
  "networking": { "ethernet": [{ "speed": 1000, "ports": 1 }] },
  "expansion": { "pmod": 1 },
  "storage": { "microsd": 1 }
}
```

SoM⇄carrier compatibility lives in [relationships](#compatibility-relationships) — a single SoM can fit on multiple carriers and vice versa.

### Kits

A **kit** is a pre-assembled SoM + carrier sold as one SKU. The kit file references its components by MPN; the SoM and carrier files carry the actual specs.

File: `kits/<vendor>/<mpn>.json`.

Required: `mpn`, `name`, `status`, `url`, `vendor`, `price`, `composition.{som, carrier}`. Both MPNs must exist in `soms/` and `carriers/` respectively.

Example — `kits/amd-xilinx/SK-KR260-G.json`:

```json
{
  "mpn": "SK-KR260-G",
  "name": "Kria KR260 Robotics Starter Kit",
  "status": "active",
  "url": "https://www.amd.com/en/products/system-on-modules/kria/k26/kr260-robotics-starter-kit.html",
  "vendor": "amd-xilinx",
  "price": { "value": 349, "currency": "USD" },
  "composition": {
    "som": "SM-K26-XCL2GC",
    "carrier": "KR260-Carrier"
  }
}
```

### FMC Cards

An **FMC card** is an FPGA Mezzanine Card (VITA 57) that plugs into an FMC site on a host (standalone board, kit, or carrier).

File: `fmc-cards/<vendor>/<mpn>.json`.

Required: `mpn`, `name`, `status`, `url`, `vendor`, `price`, `connector_type` (one of `lpc` / `hpc` / `fmcp`). Optional: `vadj_min` / `vadj_max` (V), `pcie`, `video`, `networking`, `usb`, `storage`.

Example — `fmc-cards/opsero/OP063.json`:

```json
{
  "mpn": "OP063",
  "name": "FPGA Drive FMC Gen4",
  "status": "active",
  "url": "https://opsero.com/product/fpga-drive-fmc-gen4",
  "vendor": "opsero",
  "price": { "value": 499, "currency": "USD" },
  "connector_type": "hpc",
  "vadj_min": 1.2,
  "vadj_max": 3.3,
  "pcie": [
    { "type": "M.2 M-key", "lanes": 4, "gen": 4 },
    { "type": "M.2 M-key", "lanes": 4, "gen": 4 }
  ]
}
```

Which hosts the card mates with lives in [relationships](#compatibility-relationships) (`fmc-mates`).

## Compatibility Relationships

Compatibility between entities lives under `relationships/`. There are two relationship types today:

| Folder | One file per … | What it captures |
|--------|----------------|------------------|
| `relationships/fmc-mates/<fmc-card-vendor>/<fmc-card-mpn>.json` | FMC card | The hosts (standalone boards, kits, carriers) the card mates with, and on which slot. |
| `relationships/som-mates/<carrier-vendor>/<carrier-mpn>.json` | carrier | The SoMs that physically and electrically fit on the carrier. |

The parent folder mirrors the owning entity's vendor folder — so an FMC card at `fmc-cards/opsero/OP120.json` has its compatibility list at `relationships/fmc-mates/opsero/OP120.json`, and a carrier at `carriers/avnet/AES-ZU7EV-1-CC-FMC-G.json` has its compatibility list at `relationships/som-mates/avnet/AES-ZU7EV-1-CC-FMC-G.json`. This makes it easy for each vendor to find and maintain the compatibility lists for their own products.

The filename stem (e.g. `OP120`) must match the bundle's top-level key field (`fmc_card` or `carrier`).

### FMC mates

One file per FMC card. Each entry in `compatible_hosts` describes one (host, slot) pairing.

`relationships/fmc-mates/opsero/OP120.json`:

```json
{
  "fmc_card": "OP120",
  "compatible_hosts": [
    {
      "host": "VCU118",
      "host_type": "standalone",
      "target_slot": "FMCP",
      "verified_by": "vendor",
      "notes": "2x 40G."
    },
    {
      "host": "AES-ZU7EV-1-CC-FMC-G",
      "host_type": "carrier",
      "target_slot": "HPC",
      "verified_by": "vendor"
    }
  ]
}
```

| Entry field | Required | Description |
|-------------|----------|-------------|
| `host` | yes | MPN of the host. Must exist under `boards/`, `kits/`, or `carriers/` depending on `host_type`. |
| `host_type` | yes | One of `standalone`, `kit`, or `carrier`. Drives which folder the host file lives in. |
| `target_slot` | no | Slot name on the host (matches a `slot` value in the host's `expansion.fmc[]`). Omit if the relationship applies to any slot. One entry per slot, so a host with multiple compatible FMC sites gets multiple entries. |
| `verified_by` | no | Who confirmed the mating (e.g. `"vendor"`, `"fpgadeveloper"`). |
| `notes` | no | Short free-text note (e.g. specific firmware revision, performance result). |

### SoM mates

One file per carrier, listing every SoM the carrier accepts.

`relationships/som-mates/amd-xilinx/KR260-Carrier.json`:

```json
{
  "carrier": "KR260-Carrier",
  "compatible_soms": [
    { "som": "SM-K26-XCL2GC", "verified_by": "vendor" }
  ]
}
```

| Entry field | Required | Description |
|-------------|----------|-------------|
| `som` | yes | MPN of the SoM. Must exist under `soms/`. |
| `verified_by` | no | Who confirmed the mating. |
| `notes` | no | Short free-text note. |

### Adding a compatibility entry

To record that an existing FMC card works on a new host, edit `relationships/fmc-mates/<vendor>/<card>.json` and append an entry to `compatible_hosts`. If the file doesn't exist yet (new card, or no edges recorded yet), create it. Same idea for SoM+carrier pairs in `som-mates/`.

CI validates that:

- The bundle's `fmc_card` / `carrier` key matches the filename stem.
- The parent folder matches the owning entity's `vendor` field.
- Every referenced MPN (`fmc_card`, `host`, `carrier`, `som`) exists in the corresponding entity folder.

## Notes

Per-entity markdown notes — boot-mode DIP switch tables, jumper defaults, errata, gotchas. See [`notes/README.md`](notes/README.md) for the format, what belongs there, and the link policy.

## Attributes

Per-vendor device attributes that add rows to the board detail page (ML support, tool part number, resource counts, transceiver rates, ...). See [`attributes/README.md`](attributes/README.md).

## Vendors

Board and silicon vendors are defined in `vendors.json`. Each entity references vendors by key rather than embedding vendor details inline.

### Board Vendors

<!-- BOARD-VENDORS-BEGIN — generated by scripts/update-readme.py, do not edit by hand -->
| Key | Name |
|-----|------|
| `adiuvo` | Adiuvo |
| `alinx` | Alinx |
| `altera` | Altera |
| `amd-xilinx` | AMD Xilinx |
| `arrow` | Arrow |
| `avnet` | Avnet |
| `bittware` | BittWare |
| `brisbanesilicon` | BrisbaneSilicon |
| `bunnie-studios` | Bunnie Studios |
| `cologne-chip` | Cologne Chip |
| `critical-link` | Critical Link |
| `digilent` | Digilent |
| `efinix` | Efinix |
| `enclustra` | Enclustra |
| `forgefunder` | Forgefunder |
| `gowin` | Gowin Semiconductor |
| `hitech-global` | Hitech Global |
| `imperix` | imperix |
| `intergalaktik` | Intergalaktik |
| `invent-logics` | Invent Logics |
| `iwave` | iWave Systems |
| `knjn` | KNJN |
| `knowres` | Knowledge Resources |
| `krtkl` | Krtkl |
| `lattice` | Lattice |
| `microchip` | Microchip |
| `myir` | MYIR Tech |
| `numato-lab` | Numato Lab |
| `opal-kelly` | Opal Kelly |
| `opsero` | Opsero |
| `real-digital` | Real Digital |
| `redpitaya` | RedPitaya |
| `rhs-research` | RHS Research |
| `sundance` | Sundance Multiprocessor Technology Ltd. |
| `techway` | Techway |
| `terasic` | Terasic |
| `trenz` | Trenz Electronic |
| `tria` | Tria Technologies |
| `tul` | TUL |
| `vicharak` | Vicharak |
| `vlsi-system-design` | VLSI System Design |
<!-- BOARD-VENDORS-END -->

### Silicon Vendors

<!-- SILICON-VENDORS-BEGIN — generated by scripts/update-readme.py, do not edit by hand -->
| Key | Name |
|-----|------|
| `achronix` | Achronix |
| `altera` | Altera |
| `amd-xilinx` | AMD Xilinx |
| `cologne-chip` | Cologne Chip |
| `efinix` | Efinix |
| `gowin` | Gowin Semiconductor |
| `lattice` | Lattice |
| `microchip` | Microchip |
| `quicklogic` | QuickLogic |
| `renesas` | Renesas |
<!-- SILICON-VENDORS-END -->

To add a new vendor, add an entry to the appropriate section in `vendors.json` with a kebab-case key, display name, and URL, then run `python scripts/update-readme.py` to regenerate the tables above.

### Tips

- Only include optional fields that have meaningful values. If a board has no PCIe, omit the `pcie` key entirely.
- Use the ISO 4217 currency code for the `price.currency` field (e.g. `"USD"`, `"EUR"`, `"GBP"`).
- The `mpn` should be the manufacturer part number as published by the vendor. It must be unique across all entities and contain only letters, numbers, hyphens, dots, and underscores — replace spaces, slashes, or other unsupported characters with hyphens. Drop trailing PCB-revision suffixes (e.g. `_V3.1`) so the MPN stays stable across revisions.
- The filename must match the `mpn` field exactly (e.g. a board with `"mpn": "ZCU102"` goes in `ZCU102.json`).
- Set `status` to `"active"` for entities currently available for purchase, `"nrnd"` if still available but not recommended for new designs, `"eol"` for end-of-life, or `"discontinued"` for discontinued.

## Validation

Every pull request is validated automatically by [`.github/workflows/validate.yml`](.github/workflows/validate.yml), which checks each entity (boards, SoMs, carriers, kits, FMC cards) and each relationship file against `schema.json`, enforces filename / vendor folder / MPN consistency, and rejects duplicate MPNs. You can run a quick local check against just the board files:

```bash
pip install jsonschema referencing
python -c "
import json, glob
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

with open('schema.json') as f:
    schema = json.load(f)

# Register the whole schema under a URN so internal \$refs (e.g. #/\$defs/price
# from the board sub-schema) resolve against it.
registry = Registry().with_resource('urn:root', Resource.from_contents(schema))
validator = Draft202012Validator({'\$ref': 'urn:root#/\$defs/standalone'}, registry=registry)

errors = 0
files = sorted(glob.glob('boards/**/*.json', recursive=True))
for path in files:
    with open(path) as f:
        board = json.load(f)
    board_errors = list(validator.iter_errors(board))
    if board_errors:
        print(f'{path}:')
        for e in board_errors:
            print(f'  - {e.json_path}: {e.message}')
        errors += len(board_errors)

print(f'{len(files)} boards checked, {errors} error(s)' if errors else f'{len(files)} boards checked — all valid!')
"
```

The same pattern works for the other entity folders — swap `boards` and `standalone` for `soms`/`som`, `carriers`/`carrier`, `kits`/`kit`, or `fmc-cards`/`fmc_card`. The CI workflow runs the full sweep including relationship validation and cross-references.

## Part Number Decoders

Decoders live in `parts/{vendor}/{Family}.json` — one file per FPGA family. Splitting the decoders per family makes it easier to find, review, and contribute changes without wading through a single huge file.

### File naming

The filename is derived from the family name: take the family name, replace `+` with `-Plus`, then replace any run of non-alphanumeric characters with a single `-`. Examples:

| Family | File |
|--------|------|
| `Spartan-7` | `parts/amd-xilinx/Spartan-7.json` |
| `Agilex 7` | `parts/altera/Agilex-7.json` |
| `Zynq UltraScale+ MPSoC` | `parts/amd-xilinx/Zynq-UltraScale-Plus-MPSoC.json` |
| `GW1N (LittleBee)` | `parts/gowin/GW1N-LittleBee.json` |

### Decoder format

Each file is a single family object. Fields are consumed left-to-right through the part number string. Field types:

- `fixed` — a literal substring (e.g. the family code `"7S"` in Spartan-7).
- `select` — a set of options; the longest matching option wins. Options may include a `when` clause to restrict them based on earlier field selections.

A field with `"required": false` is skipped if no option matches (used for optional speed grades, suffixes, etc.).

### Adding or editing a decoder

1. Edit the family file directly (e.g. `parts/lattice/ECP5.json`), or create a new file for a new family.
2. Open a pull request. The website's build pipeline will merge the per-family files into the deployed site automatically.

## License

This data is maintained by the community for use by [FPGA Board Repository](https://boards.fpgadeveloper.com).
