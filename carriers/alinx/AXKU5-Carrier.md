---
mpn: AXKU5-Carrier
name: AXKU5 Base Board
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Kintex-UltraScale-plus/AXKU5.html
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

The FMC HPC LA signals connect to FPGA HP banks 64/65; per the user guide (Part 3.4) the I/O level standard is 1.8 V by default. The bank supply is the carrier-generated V_ADJ rail (ETA1471 DC-DC, Part 3.11) — no jumper, system controller, or programming procedure is documented, so VADJ should be treated as fixed at 1.8 V.
