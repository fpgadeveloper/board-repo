---
mpn: AXKU3-Carrier
name: AXKU3 Base Board
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Kintex-UltraScale-plus/AXKU3.html
vendor: alinx
price: null
---

## Sensors
- Temperature LM75A

## PCIe
- Edge Gen3 x8

## Video
- MIPI CSI x1

## Networking
- 1GbE x1

## USB UART/JTAG
- Mini-B UART

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- GPIO Header x1

## Storage
- microSD x1

## User I/O
- LEDs x4
- Pushbuttons x4

## Features
- Battery-backed RTC

## Notes

The FMC HPC connector is supplied by a dedicated V_ADJ DC/DC rail, 1.8 V by default — matching the 1.8 V level standard of FMC banks 64/65. The user manual documents no jumper or programming mechanism for changing this rail, so treat VADJ as fixed at 1.8 V; the board does not read the FMC IPMI EEPROM.
