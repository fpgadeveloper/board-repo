# Notes

Per-board markdown notes that render in their own section on the board detail page. Use these for board-specific information that doesn't fit the JSON schema — boot-mode DIP switch tables, default jumper positions, jumper/strap defaults, errata, gotchas.

## File layout

```
notes/<vendor-slug>/<MPN>.md
```

The filename (minus `.md`) **must match an existing board file** at `boards/<vendor-slug>/<MPN>.json` — orphans are rejected by CI.

For example, the note for `boards/amd-xilinx/ZCU102.json` lives at `notes/amd-xilinx/ZCU102.md`.

## What belongs here

- Board-specific factual information that is genuinely useful to someone working with the board.
- Boot-mode / configuration switch tables.
- Jumper or strap default positions.
- Known issues, hardware errata, or revision-specific gotchas.
- Default IP addresses, default credentials (where vendor-published).

## What does not belong here

- **Tutorials and walkthroughs.** A note is not a getting-started guide.
- **Promotional content.** No "I wrote a blog post about this board, click here."
- **Vendor marketing copy.** Don't paste in product descriptions or feature lists — the schema already captures features.
- **Information already in the schema.** Don't restate price, FPGA part number, transceiver counts, etc.
- **Images.** Text and tables only for now.
- **Long-form prose.** Notes should be scannable. If you find yourself writing paragraphs, consider whether the information belongs in vendor documentation instead and just link to it.

## Link policy

Links are allowed **only to official vendor documentation** — the board vendor's or silicon vendor's own domain (e.g. `xilinx.com`, `digilent.com`, `latticesemi.com`), or vendor-owned GitHub organizations (e.g. `github.com/Xilinx`, `github.com/Avnet`).

No blogs, forums, personal sites, monetized content, distributors, or third-party tutorials. PRs that include such links will be rejected or have the links removed.

The reasoning: vendor docs are the authoritative source and tend to be maintained. Other links rot, change, or were spam to begin with.

## Markdown gotchas

The renderer is [Python-Markdown](https://python-markdown.github.io/) with the `tables` and `fenced_code` extensions, sanitized via [bleach](https://bleach.readthedocs.io/).

A few CommonMark rules that catch people out:

- **Lists need a blank line before them.** Otherwise the `1.` / `*` lines fold into the previous paragraph and render on a single line:

  ```markdown
  Notes:
  1. First           ← BROKEN: no blank line, will collapse
  2. Second
  ```

  ```markdown
  Notes:

  1. First           ← Correct
  2. Second
  ```

- **Heading levels** are demoted by 2 at build time so that the page's `<h3>Notes</h3>` wrapper stays at the top of the visual hierarchy. Use `## Configuration`, `## Boot Modes`, etc. as your top-level headings — they render as `<h4>` on the page.

- **Allowed HTML tags after sanitization:** `h2`–`h6`, `p`, `br`, `hr`, `strong`, `em`, `code`, `pre`, `blockquote`, `ul`, `ol`, `li`, `a`, `span`, and full table tags. Raw HTML using anything else (`<script>`, `<iframe>`, inline event handlers, `style` attributes, etc.) is stripped.

## How it's rendered

At build time, `scripts/build.py` (`build_notes()` in the website repo) reads each `.md` file, renders it to HTML, sanitizes the output, and writes the result to `data/notes/<vendor>/<MPN>.html` on the deployed site. Boards that have a note get a `_has_notes: true` flag in `data/boards.json`; the board detail page fetches the rendered HTML on demand.

You don't need to run the build locally to contribute — open a PR and CI/Netlify handle it.

## Validation

`.github/workflows/validate.yml` checks that every `notes/<vendor>/<MPN>.md` has a matching `boards/<vendor>/<MPN>.json`. Renames or deletions to a board file therefore require the matching note to be renamed or deleted in the same PR.
