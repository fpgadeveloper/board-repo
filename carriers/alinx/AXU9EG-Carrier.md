---
mpn: AXU9EG-Carrier
name: AXU9EG Base Board
status: active
url: https://www.en.alinx.com/Product/SoC-Development-Boards/Zynq-UltraScale-plus-MPSoC/AXU9EGB.html
vendor: alinx
price: null
---

## Sensors
- Temperature LM75

## M.2
- M-key

## Video
- DisplayPort x1
- MIPI CSI x1

## Networking
- 1GbE x2
- SFP+ x2

## Serial
- CAN x2
- RS-485 x2

## USB
- Type-A 3.0 host x2
- Type-A 2.0 host x2

## USB UART/JTAG
- Micro-B UART x2

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- GPIO Header x1

## Storage
- microSD x1

## User I/O
- LEDs x1
- Pushbuttons x2

## Features
- Battery-backed RTC

## Notes

The FMC user I/O (36 differential pairs) routes to SoM banks 66/67, whose VCCO is supplied by the carrier's fixed +1.8 V rail (shared with Ethernet and USB 2.0; user guide Parts 3.12 and 3.20). No jumper or programmable VADJ selection mechanism is documented, so VADJ is fixed at 1.8 V.
