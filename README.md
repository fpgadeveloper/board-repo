# FPGA Board Repository

This repository contains the community-maintained database of FPGA development boards used by [FPGA Board Finder](https://boards.fpgadeveloper.com). Contributions are welcome — if you know of an FPGA board that's missing, you can add it here.

## Files

| File | Description |
|------|-------------|
| `boards.json` | The board database — an array of FPGA development board objects. |
| `schema.json` | JSON Schema (Draft 2020-12) that validates `boards.json`. |

## How to Add a Board

### Option 1: Submit via the Website

The easiest way to add a board is through the **Submit** page on the website:

**[boards.fpgadeveloper.com/submit.html](https://boards.fpgadeveloper.com/submit.html)**

Fill in the form and your submission will be reviewed and added to the database.

### Option 2: Submit a Pull Request

If you prefer, you can add a board directly by editing `boards.json` and opening a pull request.

#### Steps

1. **Fork** this repository.
2. **Edit** `boards.json` — add your board object to the array.
3. **Validate** your changes against the schema (see [Validation](#validation) below).
4. **Open a pull request** with a brief description of the board you're adding.

#### Board Object Format

Each board is a JSON object with the following required fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (URL-safe slug, e.g. `"Arty-A7-35T"`). |
| `name` | string | Display name of the board. |
| `status` | string | `"active"` or `"eol"` (end-of-life). |
| `url` | string | Product page URL. |
| `vendor` | object | `{ "name": "Vendor Name", "url": "https://..." }` |
| `price` | object | `{ "value": 129.00, "currency": "USD" }` |
| `device` | object | FPGA/SoC device info (see below). |

The `device` object requires:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | One of: `"FPGA"`, `"SoC"`, `"MPSoC"`, `"RFSoC"`, `"ACAP"`. |
| `family` | string | Device family (e.g. `"Artix-7"`, `"Zynq UltraScale+"`). |
| `part` | string | Full part number (e.g. `"XC7A35T-1CPG236C"`). |
| `vendor` | string | Silicon vendor (e.g. `"AMD Xilinx"`, `"Intel"`, `"Lattice"`). |

Optional fields include `pcie`, `video`, `ethernet`, `networking`, `expansion`, `storage`, and `wireless`. See `schema.json` for full details on each.

#### Minimal Example

```json
{
  "id": "Arty-A7-35T",
  "name": "Arty A7-35T",
  "status": "active",
  "url": "https://digilent.com/shop/arty-a7-35t/",
  "vendor": {
    "name": "Digilent",
    "url": "https://digilent.com/"
  },
  "price": {
    "value": 129.00,
    "currency": "USD"
  },
  "device": {
    "type": "FPGA",
    "family": "Artix-7",
    "part": "XC7A35T-1CPG236C",
    "vendor": "AMD Xilinx",
    "vendor_url": "https://www.amd.com"
  }
}
```

#### Full Example (with interfaces)

```json
{
  "id": "SP701",
  "name": "SP701",
  "status": "active",
  "url": "https://www.xilinx.com/sp701",
  "vendor": {
    "name": "AMD Xilinx",
    "url": "https://www.amd.com"
  },
  "price": {
    "value": 774.00,
    "currency": "USD"
  },
  "device": {
    "type": "FPGA",
    "family": "Spartan-7",
    "part": "XC7S100-2FGGA676C",
    "vendor": "AMD Xilinx",
    "vendor_url": "https://www.amd.com"
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

### Tips

- Only include optional fields that have meaningful values. If a board has no PCIe, omit the `pcie` key entirely.
- Use the ISO 4217 currency code for the `price.currency` field (e.g. `"USD"`, `"EUR"`, `"GBP"`).
- The `id` should be unique and URL-safe (letters, numbers, hyphens).
- Set `status` to `"active"` for boards that are currently available for purchase, or `"eol"` for discontinued boards.

## Validation

You can validate your changes against the schema:

```bash
pip install jsonschema referencing
python -c "
import json
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

with open('schema.json') as f:
    schema = json.load(f)
with open('boards.json') as f:
    data = json.load(f)

resource = Resource.from_contents(schema)
registry = Registry().with_resource('', resource)
validator = Draft202012Validator(schema, registry=registry)

errors = list(validator.iter_errors(data))
if errors:
    for e in errors:
        print(f'  - {e.json_path}: {e.message}')
    print(f'{len(errors)} validation error(s)')
else:
    print('Valid!')
"
```

## License

This data is maintained by the community for use by [FPGA Board Finder](https://boards.fpgadeveloper.com).
