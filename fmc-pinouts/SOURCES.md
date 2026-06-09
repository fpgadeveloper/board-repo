# FMC pinout data — sources & attribution

The JSON files under `fmc-pinouts/` map FMC connector signals (VITA 57.1 / 57.4:
`LA*`, `HA*`, `HB*`, `CLK*`, `GBTCLK*`, `DP*`) to FPGA package pins, per board /
carrier / FMC card. The pin-assignment **values are facts** about each board's
routing, but they were derived from the third-party sources below. Each generated
file also records its origin in its own `source` / `source_ref` fields; this file
is the consolidated attribution and license notice.

We redistribute only the extracted pin-mapping data in our own JSON schema — not
the original source files. Where a source is permissively licensed, its copyright
notice and license are reproduced or linked below.

---

## litex-boards — BSD-2-Clause

Project: <https://github.com/litex-hub/litex-boards>

Used for these host pinouts (parsed from `litex_boards/platforms/<board>.py`):

| Pinout file | Platform file | Copyright holders |
|---|---|---|
| `boards/numato-lab/Nereid.json`    | `numato_nereid.py`             | © 2018–2019 Rohit Singh; © 2019 Florent Kermarrec |
| `boards/numato-lab/Tagus.json`     | `numato_tagus.py`              | © 2018–2019 Rohit Singh; © 2018 Florent Kermarrec |
| `boards/lattice/LIFCL-40-EVN.json` | `lattice_crosslink_nx_evn.py`  | © 2020 David Corrigan; © 2020 Alan Green |
| `boards/lattice/LFCPNX-EVN.json`   | `lattice_certuspro_nx_evn.py`  | © 2024 Enjoy-Digital |
| `boards/efinix/Ti375C529-DK.json`  | `efinix_ti375_c529_dev_kit.py` | © 2024 Dolu1990 (Charles Papon) |

Repository copyright: Copyright (c) 2012–2026 Enjoy-Digital; Copyright (c)
2012–2026 LiteX-Hub community. All rights reserved.

Full license text (`LICENSE`):

```
BSD 2-Clause License

Copyright (c) Copyright 2012-2026 Enjoy-Digital.
Copyright (c) Copyright 2012-2026 / LiteX-Hub community.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## AMD / Xilinx Board Store — Apache License 2.0

Project: <https://github.com/Xilinx/XilinxBoardStore>

Used for these host pinouts (parsed from each board's `board.xml` +
`part0_pins.xml`): `boards/amd-xilinx/` — ZCU102, ZCU104, ZCU106, KCU105,
KCU116, KC705, ZC702, ZC706, AC701, VCU108.

Copyright (C) 2019, Xilinx Inc — All rights reserved. Licensed under the Apache
License, Version 2.0. License text: <http://www.apache.org/licenses/LICENSE-2.0>
