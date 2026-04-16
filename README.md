# FPGA Board Repository

This repository contains the community-maintained database of FPGA development boards used by [FPGA Board Repository](https://boards.fpgadeveloper.com). Contributions are welcome — if you know of an FPGA board that's missing, you can add it here.

## Files

| Path | Description |
|------|-------------|
| `boards/` | Individual board JSON files, organized by vendor (e.g. `boards/amd-xilinx/ZCU102.json`). |
| `parts/` | Part-number decoder files, one per family (e.g. `parts/amd-xilinx/Spartan-7.json`). |
| `vendors/` | Per-vendor reference data (tool part rules, device resources, transceivers, package info). |
| `vendors.json` | Centralized registry of board vendors and silicon vendors. |
| `schema.json` | JSON Schema (Draft 2020-12) that validates individual board objects. |

## How to Add a Board

### Option 1: Submit via the Website

The easiest way to add a board is through the **Submit** page on the website:

**[boards.fpgadeveloper.com/submit.html](https://boards.fpgadeveloper.com/submit.html)**

Fill in the form and your submission will be reviewed and added to the database.

### Option 2: Submit a Pull Request

If you prefer, you can add a board directly by creating a new JSON file and opening a pull request.

#### Steps

1. **Fork** this repository.
2. **Create** a new file at `boards/<vendor-slug>/<board-id>.json` with your board object.
3. **Validate** your changes against the schema (see [Validation](#validation) below).
4. **Open a pull request** with a brief description of the board you're adding.

#### Board Object Format

Each board is a JSON object with the following required fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier, typically the ordering part number without spaces (e.g. `"ZCU102"`). |
| `name` | string | Display name of the board. |
| `status` | string | `"active"`, `"eol"` (end-of-life), or `"discontinued"`. |
| `url` | string | Product page URL. |
| `vendor` | string | Board vendor key (must match a key in `vendors.json` `board_vendors`). |
| `price` | object | `{ "value": 129.00, "currency": "USD" }` |
| `device` | object | FPGA/SoC device info (see below). |

The `device` object requires:

| Field | Type | Description |
|-------|------|-------------|
| `part` | string | Full orderable part number (e.g. `"XC7A35T-1CPG236C"`). |
| `vendor` | string | Silicon vendor key (must match a key in `vendors.json` `silicon_vendors`). |

Optional fields include `pcie`, `video`, `ethernet`, `networking`, `expansion`, `storage`, and `wireless`. See `schema.json` for full details on each.

#### Example

Create a file at `boards/digilent/Arty-A7.json`:

```json
{
  "id": "Arty-A7",
  "name": "Arty A7",
  "status": "active",
  "url": "https://digilent.com/shop/arty-a7/",
  "vendor": "digilent",
  "price": {
    "value": 129.00,
    "currency": "USD"
  },
  "device": {
    "part": "XC7A35T-1CPG236C",
    "vendor": "amd-xilinx"
  }
}
```

#### Example with Interfaces

`boards/amd-xilinx/SP701.json`:

```json
{
  "id": "SP701",
  "name": "SP701",
  "status": "active",
  "url": "https://www.xilinx.com/sp701",
  "vendor": "amd-xilinx",
  "price": {
    "value": 774.00,
    "currency": "USD"
  },
  "device": {
    "part": "XC7S100-2FGGA676C",
    "vendor": "amd-xilinx"
  },
  "video": {
    "hdmi_out": 1,
    "mipi_dsi": 1,
    "mipi_csi": 1
  },
  "ethernet": [
    { "speed": 1000, "ports": 2 }
  ],
  "expansion": {
    "fmc_lpc": 1,
    "pmod": 6
  }
}
```

## Vendors

Board and silicon vendors are defined in `vendors.json`. Each board references vendors by key rather than embedding vendor details inline.

### Board Vendors

| Key | Name |
|-----|------|
| `alinx` | Alinx |
| `amd-xilinx` | AMD Xilinx |
| `avnet` | Avnet |
| `bittware` | BittWare |
| `digilent` | Digilent |
| `efinix` | Efinix |
| `hitech-global` | Hitech Global |
| `imperix` | imperix |
| `invent-logics` | Invent Logics |
| `knjn` | KNJN |
| `krtkl` | Krtkl |
| `lattice` | Lattice |
| `myir` | MYIR Tech |
| `numato-lab` | Numato Lab |
| `opal-kelly` | Opal Kelly |
| `real-digital` | Real Digital |
| `redpitaya` | RedPitaya |
| `rhs-research` | RHS Research |
| `sundance` | Sundance Multiprocessor Technology Ltd. |
| `terasic` | Terasic |
| `trenz` | Trenz Electronic |
| `tria` | Tria Technologies |
| `tul` | TUL |

### Silicon Vendors

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

To add a new vendor, add an entry to the appropriate section in `vendors.json` with a kebab-case key, display name, and URL.

### Tips

- Only include optional fields that have meaningful values. If a board has no PCIe, omit the `pcie` key entirely.
- Use the ISO 4217 currency code for the `price.currency` field (e.g. `"USD"`, `"EUR"`, `"GBP"`).
- The `id` should be unique and contain only letters, numbers, hyphens, dots, and underscores.
- The filename should match the board ID (e.g. board with `"id": "ZCU102"` goes in `ZCU102.json`).
- Set `status` to `"active"` for boards currently available for purchase, `"eol"` for end-of-life boards, or `"discontinued"` for discontinued boards.

## Validation

You can validate individual board files against the schema:

```bash
pip install jsonschema referencing
python -c "
import json, glob
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

with open('schema.json') as f:
    schema = json.load(f)

board_schema = schema['\$defs']['board']
resource = Resource.from_contents(schema)
registry = Registry().with_resource('', resource)
validator = Draft202012Validator(board_schema, registry=registry)

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
