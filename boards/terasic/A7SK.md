---
mpn: A7SK
name: Agilex 7 FPGA Starter Kit
status: active
url: https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=142&No=1295
vendor: terasic
price: { value: 5491, currency: USD }
device: { part: AGFB027R24C2E2VC, vendor: altera }
---

## Memory
- DDR4 8GB 72-bit ECC SODIMM
- DDR4 8GB 72-bit ECC

## Sensors
- Temperature

## Clocking
- Programmable

## PCIe
- Edge Gen4 x8

## Video
- HDMI Out x1

## Networking
- 1GbE x1
- QSFP28 x1

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC+ "FMCP" VADJ 1.2V
- GPIO Header x1

## Storage
- microSD x1

## User I/O
- LEDs x2
- Pushbuttons x2
- DIP switches x2

## Features
- Power monitoring

## Extras
- On-board USB-Blaster II; AS x4 configuration from on-board QSPI flash (1 Gbit or 2 Gbit depending on board build)
- MAX 10 board management controller with power monitoring, temperature monitoring and automatic fan control
- 2x4 12V auxiliary power connector, plus a power switch for stand-alone (non-slot) operation
- HPS-side user LED x1, push-button x1 and cold-reset button, in addition to the FPGA-side user I/O
- FMC+ site carries 181 FPGA I/O and 16 transceivers (16 Gbps tested maximum), with four programmable FMC+ transceiver reference clocks
- HDMI 2.1 output supports TMDS up to 4K@60 and FRL6 up to 4K@120

## Notes

The FPGA-side DDR4 SO-DIMM socket (DDR4-A) is shared with the HPS: it can be driven by the HPS EMIF or, when the HPS EMIF is unused, by the FPGA fabric. The on-board 8 GB DDR4-B bank is always FPGA-fabric side. The socket accepts up to a 16 GB single-rank SO-DIMM; the kit ships with an 8 GB ECC module.

Configuration mode is set by the two MSEL slide switches:

| Mode | MSEL2 | MSEL1 | MSEL0 |
|---|---|---|---|
| AS Fast (default) | 0 | 0 | 1 |
| JTAG | 1 | 1 | 1 |

Other default settings worth knowing before first power-on:

- **PCIe presence detect** — a DIP switch selects x1 / x4 / x8 presence detect; the default is x8 detect enabled, x1 and x4 disabled.
- **JTAG bypass** — both positions of the JTAG bypass switch default to ON, which keeps the HPS and the FMC+ connector *out* of the board JTAG chain. Switching a position OFF without a JTAG device present on that branch breaks the chain and Quartus will no longer detect the FPGA.
- **Force external power** — this switch defaults to ON, so the 2x4 12 V auxiliary power connector must be attached even when the card sits in a host PCIe slot, otherwise the board will not power up.
- **FMC_VCCIO select header (JP1)** — a 3-pin jumper sets `VCCIO_FMCP_HAB`, the VCCIO of the FPGA bank serving the FMC+ HA/HB pins and CLK1_M2C, to 1.2 V (default) or 1.5 V.
  This is a host-side bank rail only — it does **not** change VADJ: the FMC+ connector's VADJ rail is fixed at 1.2 V (4 A max), and the FMC+ LA-bank I/O is fixed at 1.2 V, so a mezzanine always sees 1.2 V VADJ regardless of the jumper.
  The user manual calls this header JP1 in one section and JP2 / JP3 in two others; the board silkscreen reads JP1.

The factory SoC boot flow is FPGA-configuration-first: the SDM loads its firmware, the FPGA image and the HPS first-stage boot loader from the QSPI flash, then the second-stage boot loader, kernel and root filesystem come from the microSD card.

Earlier board revisions shipped earlier steppings of the same device — AGFB027R24C2E2V and AGFB027R24C2E2VB, both now EOL. Current boards carry AGFB027R24C2E2VC.
