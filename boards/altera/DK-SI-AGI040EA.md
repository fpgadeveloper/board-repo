---
mpn: DK-SI-AGI040EA
name: Agilex 7 I-Series Transceiver (6x F-Tile)
status: active
url: https://www.altera.com/products/devkit/po-3014/agilex-7-fpga-i-series-transceiver-development-kit-6x-f-tile
vendor: altera
price: { value: 14995, currency: USD }
device: { part: AGIC040R39A1E1VC, vendor: altera }
---

## Memory
- DDR4 16GB 72-bit ECC DIMM
- DDR4 16GB 72-bit ECC

## Clocking
- Programmable

## PCIe
- MCIO Gen4 x4

## Networking
- SFP x1
- QSFP x3
- QSFP-DD x4
- QSFP-DD800 x1
- OSFP x1

## USB
- Type-B 2.0 device

## USB UART/JTAG
- Type-B JTAG

## Expansion
- FMC+ "FMCP1" VADJ 1.2V
- FMC+ "FMCP2" VADJ 1.2V

## Features
- Power monitoring

## Notes

VADJ on both FMC+ slots (FMC-A J7, FMC-B J9) is fixed at 1.2 V by a factory-fitted 0 Ω strap to the 1.2 V rail (R1122 / R1180); an unpopulated 0 Ω option (R1123 / R1181) allows re-strapping to 1.8 V by board rework only. There is no jumper and no IPMI-based auto-negotiation — the slots carry 16 FGT transceiver lanes each plus all 34 LA pairs, routed straight to the FPGA's 1.2 V banks in the default build (MAX3378E level translators for a 1.8 V VADJ are present but not populated; using them is a board-rework option paired with the 1.8 V strap). A schematic design note next to the strap warns "SUPPORT ONLY FOR SPECIFIC 1.8V IO STANDARD FMC+ CARDS."
