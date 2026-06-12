---
mpn: AM-PE5-W
name: Andromeda PE5
status: active
url: https://www.enclustra.com/en/products/base-boards/andromeda-pe5/
vendor: enclustra
price: null
---

## Clocking
- Programmable

## PCIe
- Edge x8

## M.2
- M-key PCIe+SATA

## Networking
- 1GbE x2 RJ45-only
- SFP28 x2
- QSFP28 x1

## Video
- HDMI In x1
- HDMI Out x1
- DisplayPort x1
- SDI In x2
- SDI Out x2

## USB
- Type-C 3.0 host x2

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC+ "FMC0" VADJ 1.2-3.3V
- FMC+ "FMC1" VADJ 1.2-3.3V

## Storage
- microSD x1

## Features
- Power monitoring

## Notes

Each FMC+ slot has an independent VADJ rail (V_ADJ_F0 / V_ADJ_F1) selected by DIP switches VSEL0 / VSEL1 (switches 1-3): OFF, 1.2 V, 1.5 V, 1.72 V, 1.8 V, 2.5 V or 3.3 V; factory default 1.8 V. The board's OVP circuit disables a rail set above the module's advertised maximum, but the FMC IPMI EEPROM is not read - the user must set the switches to match the FMC card.
