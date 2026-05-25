# FPGA Board Repository

This repository contains the community-maintained database of FPGA development boards, system-on-modules, carriers, kits, and FMC mezzanine cards used by [FPGA Board Repository](https://boards.fpgadeveloper.com). Contributions are welcome — if you know of an entity that's missing, you can add it here.

## Files

| Path | Description |
|------|-------------|
| `boards/` | Standalone FPGA boards (the FPGA, memory, peripherals, and I/O all on one PCB). One markdown file per board, organized by vendor (e.g. `boards/amd-xilinx/ZCU102.md`). |
| `soms/` | System-on-modules — small daughter boards carrying the FPGA, memory, and flash, designed to plug into a carrier (e.g. `soms/amd-xilinx/SM-K26-XCL2GC.md`). |
| `carriers/` | Carrier boards that host a SoM and supply power + I/O (e.g. `carriers/amd-xilinx/KR260-Carrier.md`). |
| `kits/` | Pre-assembled SoM + carrier bundles sold as a single SKU. Each kit references its components by MPN (e.g. `kits/amd-xilinx/SK-KR260-G.md`). |
| `fmc-cards/` | FPGA Mezzanine Cards (VITA 57: LPC / HPC / FMC+) that plug into FMC sites on a host (e.g. `fmc-cards/opsero/OP120.md`). |
| `relationships/` | Compatibility relationships between entities (which FMC cards mate with which hosts; which SoMs fit which carriers). Still JSON — purely relational data. See [Compatibility Relationships](#compatibility-relationships) below. |
| `parts/` | Part-number decoder files, one JSON file per FPGA family (e.g. `parts/amd-xilinx/Spartan-7.json`). See [Part Number Decoders](#part-number-decoders) below. |
| `attributes/` | Per-vendor device attributes that extend the board detail page (ML support, resource counts, transceivers, ...). JSON. See [`attributes/README.md`](attributes/README.md). |
| `MARKDOWN_FORMAT.md` | Canonical specification of the entity markdown format — what the strict parser accepts, section by section. |
| `schema.json` | JSON Schema (Draft 2020-12) — the data contract the parsed markdown must satisfy. |
| `vendors.json` | Centralized registry of board vendors and silicon vendors. |
| `scripts/json_from_md.py` | The strict markdown → JSON parser. CI runs it; the website build imports it. |

## Entity files are markdown

Each board, SoM, carrier, kit, and FMC card is a **markdown file** — YAML front-matter for identity fields (MPN, name, vendor, price, device, ...), then `## Section` headings with one bullet per feature:

```markdown
---
mpn: SP701
name: SP701
status: active
url: https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/sp701.html
vendor: amd-xilinx
price: { value: 836, currency: USD }
device: { part: XC7S100-2FGGA676C, vendor: amd-xilinx }
---

## Memory
- DDR3L 512MB 16-bit

## Video
- HDMI Out x1
- MIPI DSI x1
- MIPI CSI x1

## Networking
- 1GbE x2

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC LPC "LPC" VADJ 1.8-3.3V
- Pmod x6
```

[`MARKDOWN_FORMAT.md`](MARKDOWN_FORMAT.md) is the canonical reference: it lists every section, the exact bullet grammar for each, and a worked example for all five entity types. `schema.json` is the data contract behind it. The build pipeline parses the markdown into JSON for the website; **the markdown is the source of truth — there is no per-entity JSON in the repo.**

### Anything the schema doesn't model

A core principle: the markdown accepts **more** than the schema models. If a board has a feature with no schema field (a BMC, a crypto offload, a proprietary debug header), park it under `## Extras` — the parser preserves it verbatim, it just doesn't reach the website until the schema grows to cover it. Free-form prose (boot-mode tables, jumper defaults, errata) goes under `## Notes`. Neither section needs to follow any grammar.

You don't have to write perfectly canonical bullets on your first push. Write what makes sense; the maintainer's PR-processing step canonicalizes near-miss bullets before merge.

## How to Contribute

Spotted a board, SoM, carrier, kit, or FMC card that's missing? There are three ways to add it — and for the first two, all you need is the vendor's product page URL. You don't have to write any markdown or fill in specs; the maintainer reads the product page and builds the catalog entry for you.

### Option 1: Submit via the website

The simplest way — paste the vendor's product page URL into the **Submit** page:

**[boards.fpgadeveloper.com/submit.html](https://boards.fpgadeveloper.com/submit.html)**

That's the whole form. Your submission is logged as an issue here, then reviewed and added.

### Option 2: Open a GitHub issue

Prefer to stay on GitHub, or want to add several boards at once? [**Open an issue**](https://github.com/fpgadeveloper/board-repo/issues/new) and include the product page URL(s) — one or many. It's imported exactly the same way as a website submission. Browse [existing issues](https://github.com/fpgadeveloper/board-repo/issues) first to avoid duplicates.

### Option 3: Submit a pull request

If you'd rather write the entry yourself — or you're correcting an existing one:

1. **Fork** this repository.
2. **Create or edit** the relevant `.md` file under the matching entity folder. The filename stem must equal the `mpn`, and the parent folder must equal the `vendor`.
3. **Check the format** against [`MARKDOWN_FORMAT.md`](MARKDOWN_FORMAT.md), or run the local validation (see [Validation](#validation) below).
4. **Open a pull request** with a brief description.

## Entity Types

All five entity types share the same markdown shape — front-matter plus feature sections. They differ in which front-matter fields are required and which sections apply. See [`MARKDOWN_FORMAT.md`](MARKDOWN_FORMAT.md) for the full per-type field set and examples.

- **Boards** (`boards/`) — a standalone board is a single PCB carrying the FPGA, memory, flash, and I/O. It runs without a separate carrier. Front-matter includes `device`; all feature sections apply.

- **SoMs** (`soms/`) — a system-on-module is a small daughter board carrying the FPGA, memory, and flash; it plugs into a carrier. Front-matter includes `device`. Most SoMs list only `## Memory` + `## Flash`; the schema also allows a few SoM-edge peripherals for modules that bring their own (the Avnet MicroZed carries its own Ethernet, USB, and a Pmod). `## PCIe`, `## High-speed I/O`, `## Video`, and `## Display` are carrier-side only.

- **Carriers** (`carriers/`) — a carrier hosts a SoM and exposes its I/O plus power. Front-matter omits `device`; all feature sections apply. Use `price: null` for carriers sold only inside a kit, and give them a stable MPN such as `<kit-mpn>-Carrier`.

- **Kits** (`kits/`) — a kit is a pre-assembled SoM + carrier sold as one SKU. Front-matter omits `device` and adds `composition: { som: <mpn>, carrier: <mpn> }` — both MPNs must exist under `soms/` and `carriers/`. A kit has no feature sections; its specs come from the composed SoM + carrier. Bundled extras (cables, PSUs) go under a `## Includes` section.

- **FMC cards** (`fmc-cards/`) — an FMC card is an FPGA Mezzanine Card (VITA 57) that plugs into an FMC site on a host. Front-matter omits `device` and adds `connector_type` (`lpc` / `hpc` / `fmcp`) plus optional `vadj_min` / `vadj_max`.

Which FMC cards mate with which hosts, and which SoMs fit which carriers, lives under [`relationships/`](#compatibility-relationships) — not in the entity files themselves.

## Compatibility Relationships

Compatibility between entities lives under `relationships/`. These files stay **JSON** — they're purely relational, bidirectional data, not the kind of thing a typical contributor hand-edits. There are two relationship types today:

| Folder | One file per … | What it captures |
|--------|----------------|------------------|
| `relationships/fmc-mates/<fmc-card-vendor>/<fmc-card-mpn>.json` | FMC card | The hosts (standalone boards, kits, carriers) the card mates with, and on which slot. |
| `relationships/som-mates/<carrier-vendor>/<carrier-mpn>.json` | carrier | The SoMs that physically and electrically fit on the carrier. |

The parent folder mirrors the owning entity's vendor folder — so an FMC card at `fmc-cards/opsero/OP120.md` has its compatibility list at `relationships/fmc-mates/opsero/OP120.json`, and a carrier at `carriers/tria/AES-ZUEV-CC-G.md` has its list at `relationships/som-mates/tria/AES-ZUEV-CC-G.json`. This makes it easy for each vendor to maintain compatibility lists for their own products.

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
      "host": "AES-ZUEV-CC-G",
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
| `target_slot` | no | Slot name on the host (matches a slot name in the host's `## Expansion` FMC bullets). Omit if the relationship applies to any slot. One entry per slot. |
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

To record that an existing FMC card works on a new host, edit `relationships/fmc-mates/<vendor>/<card>.json` and append an entry to `compatible_hosts`. If the file doesn't exist yet, create it. Same idea for SoM+carrier pairs in `som-mates/`.

CI validates that:

- The bundle's `fmc_card` / `carrier` key matches the filename stem.
- The parent folder matches the owning entity's `vendor` field.
- Every referenced MPN (`fmc_card`, `host`, `carrier`, `som`) exists in the corresponding entity folder.

## Notes

Board-specific prose that doesn't fit the schema — boot-mode DIP switch tables, default jumper positions, errata, gotchas — goes in a `## Notes` section at the bottom of the entity's `.md` file. It's free-form markdown (paragraphs, tables, lists) and is rendered to HTML on the board detail page. There is no separate notes file.

## Attributes

Per-vendor device attributes that add rows to the board detail page (ML support, tool part number, resource counts, transceiver rates, ...). JSON, unchanged by the markdown migration. See [`attributes/README.md`](attributes/README.md).

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
| `analog-devices` | Analog Devices |
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
| `proyecto-ciaa` | Proyecto CIAA |
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

- Only include sections that apply. If a board has no PCIe, omit the `## PCIe` section entirely.
- Use the ISO 4217 currency code for `price.currency` (e.g. `USD`, `EUR`, `GBP`).
- The `mpn` should be the manufacturer part number as published by the vendor. It must be unique across all entities and contain only letters, numbers, hyphens, dots, and underscores — replace spaces, slashes, or other unsupported characters with hyphens. Drop trailing PCB-revision suffixes (e.g. `_V3.1`) so the MPN stays stable across revisions.
- The filename must match the `mpn` field exactly (e.g. a board with `mpn: ZCU102` goes in `ZCU102.md`).
- Set `status` to `active` for entities currently available for purchase, `nrnd` if still available but not recommended for new designs, `eol` for end-of-life, or `discontinued` for discontinued.

## Validation

Every pull request is validated automatically by [`.github/workflows/validate.yml`](.github/workflows/validate.yml). It parses each entity `.md` with the strict parser (`scripts/json_from_md.py`), validates the resulting JSON against `schema.json`, enforces filename / vendor folder / MPN consistency, rejects duplicate MPNs, and cross-checks kit compositions and relationship references.

A bullet in a known section that doesn't match the canonical grammar **fails** CI — but an unknown section heading and anything under `## Extras` do not. Don't worry about getting every bullet perfectly canonical; the maintainer's PR-processing step cleans up near-miss bullets before merge.

Run the same check locally:

```bash
pip install jsonschema referencing pyyaml
python - <<'PY'
import json, glob, sys
sys.path.insert(0, "scripts")
from json_from_md import parse
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

with open("schema.json") as f:
    schema = json.load(f)
registry = Registry().with_resource("urn:root", Resource.from_contents(schema))

FOLDERS = {"boards": "standalone", "soms": "som", "carriers": "carrier",
           "kits": "kit", "fmc-cards": "fmc_card"}
errors = 0
for folder, defname in FOLDERS.items():
    validator = Draft202012Validator({"$ref": f"urn:root#/$defs/{defname}"}, registry=registry)
    for path in sorted(glob.glob(f"{folder}/**/*.md", recursive=True)):
        result = parse(open(path, encoding="utf-8").read(), defname)
        for w in result.warnings:
            print(f"{path}: warning: {w}")
        for e in validator.iter_errors(result.data):
            print(f"{path}: {e.json_path}: {e.message}")
            errors += 1
print(f"{errors} schema error(s)" if errors else "all valid!")
PY
```

`python scripts/json_from_md.py --check boards/` reports parser warnings for a whole tree without the schema step.

## Part Number Decoders

Decoders live in `parts/{vendor}/{Family}.json` — one JSON file per FPGA family. Splitting the decoders per family makes it easier to find, review, and contribute changes without wading through a single huge file.

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
