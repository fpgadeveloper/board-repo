---
mpn: LIFCL-40-EVN
name: LIFCL-40-EVN
status: active
url: https://www.latticesemi.com/en/Products/DevelopmentBoardsAndKits/CrossLink-NXEvaluationBoard
vendor: lattice
price: { value: 132, currency: USD }
device: { part: LIFCL-40-9BG400C, vendor: lattice }
---

## PCIe
- Edge Gen2 x1

## Video
- MIPI CSI x2

## USB UART/JTAG
- Mini-B JTAG

## Expansion
- FMC LPC "LPC" VADJ 1.5-3.3V
- Pmod x2
- Raspberry Pi x1

## Notes

VADJ for the FMC LPC slot supports 1.5 V / 1.8 V / 2.5 V / 3.3 V (discrete values; default 1.5 V with no jumper fitted). Selected by jumpers on the VADJ regulator's feedback divider: JP8 = 1.8 V, JP7 = 2.5 V, JP6 = 3.3 V — fit at most one jumper at a time. The FMC IPMI EEPROM is not consulted.
