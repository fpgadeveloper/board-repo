---
mpn: ME-ST1-W
name: Mercury+ ST1
status: active
url: https://www.enclustra.com/en/products/base-boards/mercury-st1/
vendor: enclustra
price: { value: 375, currency: USD }
---

## Clocking
- Programmable

## Networking
- 1GbE x2 RJ45-only
- SFP+ x1

## Video
- HDMI Out x1
- DisplayPort x1
- MIPI CSI x2
- MIPI DSI x1

## USB
- Type-A 3.0 host
- Type-B 3.0 device

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC HPC "HPC0" VADJ 1.2-3.3V

## Storage
- microSD x1

## Extras
- 2x Anios 40-pin I/O extension headers
- 3x 12-pin I/O connectors

## Notes

FMC VADJ (VCC_FMC_ADJ) is fed from the VCC_IO_B rail, selected by the I/O voltage selection jumpers on J1602: 1.2 V (VCC_1V2), 3.3 V (VCC_3V3), or the module-dependent VCC_OUT_A / VCC_OUT_B supplies (supported envelope 1.2-3.3 V). The factory default jumper positions apply no I/O voltage, so the VADJ rail is unpowered until the jumpers are set; the board does not read the FMC IPMI EEPROM.
