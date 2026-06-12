---
mpn: ME-PE3-C
name: Mercury+ PE3
status: active
url: https://www.enclustra.com/en/products/base-boards/mercury-pe3/
vendor: enclustra
price: { value: 1125, currency: USD }
---

## PCIe
- Edge x8

## M.2
- M-key PCIe+SATA

## Clocking
- Programmable

## Networking
- 1GbE x2 RJ45-only
- QSFP+ x1

## High-speed I/O
- FireFly

## Video
- HDMI Out x1
- DisplayPort x1

## USB
- Type-A 3.0 host
- Type-C 3.0 OTG

## USB UART/JTAG
- Micro-B JTAG/UART

## Storage
- microSD x1

## Expansion
- FMC HPC "FMC1" VADJ 1.2-3.3V

## Extras
- Mercury module connectors
- Low-jitter clock generator
- FTDI USB 2.0 High-Speed device controller
- System controller with USB JTAG/UART
- USB Type-C 3.0 interface carries DisplayPort and can power the board
- 12V single supply or USB-C powered
- Standalone or PCIe operation

## Notes

The available features depend on the equipped Mercury FPGA/SoC module. The base PE3 variant populates the QSFP+ cage and FMC HPC connector but omits the four SFP+ cages fitted on the PE3-4S variant.

FMC VADJ (VCC_FMC_ADJ) follows the VCC_IO_BC rail, selected by the I/O voltage selection jumpers on J2100: 1.2 V (VCC_1V2), 3.3 V (VCC_3V3), or the module-dependent VCC_OUT_A / VCC_OUT_B supplies (supported envelope 1.2-3.3 V). The factory default jumper positions apply no I/O voltage at all, so the VADJ rail is unpowered until the jumpers are set; the board does not read the FMC IPMI EEPROM.
