# Attributes

Per-vendor device attributes that extend the board detail page with extra rows.

Each attribute is a JSON file under `attributes/<silicon-vendor-slug>/` and describes **how to look up or compute one value from a decoded part number**. The build step bundles all files under a vendor into a single `data/attributes/<vendor>.json`.

## Why

Extra information about a silicon device (ML tool support, tool part number, LUT/FF/BRAM counts, I/O pin counts, transceiver rates...) lives in many places. Rather than writing one-off JSON files and hand-coded JS getters for each new piece of data, contributors drop an attribute file in the right folder and it appears on every matching board's detail page automatically.

## Files

### `<vendor>/<attribute-id>.json`

One attribute per file. Filename (minus `.json`) is arbitrary but should match the attribute's `id`.

Three shapes are supported:

**Lookup attribute** — values keyed by a template-derived key:

```json
{
  "id": "ml_standard_support",
  "label": "ML Standard Support",
  "section": "Vivado",
  "order": 20,
  "format": "boolean-yes-no",
  "key_template": "{product_grade}{family}{density}{device_type}",
  "default": false,
  "values": {
    "XC7A100T": true,
    "XC7Z020": true
  }
}
```

**Compute attribute** — value templated from decoded fields, with optional family-specific rules:

```json
{
  "id": "tool_part",
  "label": "Tool Part",
  "section": "Vivado",
  "order": 10,
  "format": "string",
  "copyable": true,
  "compute": [
    {
      "families": ["Artix-7", "Kintex-7", "Virtex-7", "Spartan-7", "Zynq-7000"],
      "template": "{product_grade}{family}{density}-{package}-{speed}",
      "transform": "lowercase"
    }
  ]
}
```

**Hybrid (per-family key + lookup values + multi-row)** — used for transceivers, where the key is built differently per family and each device produces multiple rows:

```json
{
  "id": "transceivers",
  "label": "Transceivers",
  "section": "Device",
  "order": 140,
  "format": "lines",
  "compute_key": [
    { "families": ["Artix-7", "..."], "template": "{product_grade}{family}{density}{package}-{speed}" },
    { "families": ["Versal AI Edge"],   "template": "{product_grade}{versal}{series}{device_number}{ball_pitch}{lid}{rohs}{footprint}-{speed_grade}" }
  ],
  "values": {
    "XC7Z035FFG676-2": ["8 (GTX, 6.6 Gb/s max)"]
  }
}
```

Each file must have **exactly one** of `values` (possibly with `compute_key`) or `compute`.

### Fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | yes | Unique attribute id (snake_case). |
| `label` | yes | Row label shown on the board detail page. |
| `section` | no | Section heading (default `"Device"`). New section names auto-appear; ordering is set by `_sections.json`. |
| `order` | no | Integer — relative row order within a section. Lower numbers come first; unset attributes sort last. |
| `format` | no | Value formatter. Supported: `"boolean-yes-no"`, `"number"`, `"string"` (default), `"lines"` (array → one row per element, label repeated). |
| `copyable` | no | `true` to render a copy-to-clipboard button next to the value. |
| `description` | no | Human-readable description of the attribute (for contributor reference). |
| `key_template` | lookup only | Single template applied regardless of family. Mutually exclusive with `compute_key`. |
| `compute_key` | lookup only | Array of `{families?, template}` rules building the lookup key per family. First match wins. |
| `values` | lookup only | Map from computed key (uppercased) → attribute value (scalar or array for `format: "lines"`). |
| `default` | lookup only | Value used when the key is not in the map. If omitted, the row is hidden when unmatched. |
| `compute` | compute only | Ordered list of `{families?, template, transform?}` rules that produce the final display string directly. First matching rule wins. |

### Templates

Templates use `{field_id}` placeholders that are replaced with the decoded part-number field of that id. Undefined fields expand to empty string. Decoder metadata fields are prefixed with underscore and can also be referenced: `_family`, `_vendor`, `_type`.

Example — the 7-series / UltraScale+ / Versal shared key template:

```
{product_grade}{family}{density}{device_type}{generation}{versal}{series}{device_number}
```

produces:
- `XC7A100T` for `XC7A100T-2FGG484I` (Artix-7)
- `XCZU7EV` for `XCZU7EV-2FFVC1156I` (Zynq US+)
- `XCVE2302` for `XCVE2302-1LSESFVA784` (Versal AI Edge)

### `<vendor>/_sections.json`

Optional. Controls section ordering on the board detail page. Sections not listed here are appended in insertion order.

```json
{ "order": ["Device", "Vivado"] }
```

If absent, all attributes fall back to a single `"Device"` section.
