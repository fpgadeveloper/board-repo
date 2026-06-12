---
mpn: AXAU25-Carrier
name: AXAU25 Base Board
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Artix-UltraScale-plus/AXAU25.html
vendor: alinx
price: null
---

## EEPROM
- data I2C 4Kbit 24LC04

## Sensors
- Temperature LM75

## PCIe
- Edge Gen3 x4

## Networking
- 1GbE x1

## USB UART/JTAG
- Mini-B UART

## Expansion
- FMC HPC "HPC" VADJ 1.2-1.8V
- GPIO Header x2

## Storage
- microSD x1

## User I/O
- LEDs x2
- Pushbuttons x2

## Notes

VADJ for the FMC HPC connector is one of four outputs of the carrier's ETA1471FT2G DC/DC converters and defaults to 1.8 V; a jumper cap selects 1.2 V instead (discrete 1.2 V / 1.8 V — the board does not read the FMC IPMI EEPROM). The FMC LA signals connect to FPGA banks 64/65 on the SoM, which operate at 1.8 V.
