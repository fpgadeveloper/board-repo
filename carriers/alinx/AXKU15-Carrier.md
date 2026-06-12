---
mpn: AXKU15-Carrier
name: AXKU15 Base Board
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Kintex-UltraScale-plus/AXKU15.html
vendor: alinx
price: null
---

## EEPROM
- data I2C 4Kbit 24LC04

## Sensors
- Temperature LM75

## PCIe
- Edge Gen3 x16

## Video
- MIPI CSI x2

## Networking
- 1GbE x1
- QSFP28 x2

## USB UART/JTAG
- Mini-B UART

## Expansion
- FMC HPC "HPC0" VADJ 1.8V
- FMC HPC "HPC1" VADJ 1.8V

## Storage
- microSD x1

## User I/O
- LEDs x4
- Pushbuttons x4

## Notes

Each FMC HPC slot has its own VADJ rail (FMC1_VADJ from an ETA1471, FMC2_VADJ from an SGM61163), both 1.8 V by default — matching the 1.8 V level standard of the FMC banks. The user manual documents no jumper or programming mechanism for changing these rails, so treat VADJ as fixed at 1.8 V; the board does not read the FMC IPMI EEPROM.
