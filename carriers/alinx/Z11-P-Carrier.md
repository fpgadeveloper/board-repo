---
mpn: Z11-P-Carrier
name: Z11-P Base Board
status: active
url: https://www.en.alinx.com/Product/SoC-Development-Boards/Zynq-UltraScale-plus-MPSoC/Z11-P.html
vendor: alinx
price: null
---

## EEPROM
- data I2C 4Kbit 24LC04

## Sensors
- Temperature LM75

## PCIe
- Edge Gen3 x8

## M.2
- M-key

## Video
- DisplayPort x1

## Networking
- 1GbE x2

## USB
- Type-C 3.0 OTG

## USB UART/JTAG
- Micro-B UART x2

## Expansion
- FMC HPC "HPC" VADJ 1.2-1.8V
- GPIO Header x1

## Storage
- microSD x1

## User I/O
- LEDs x1
- Pushbuttons x2

## Notes

FMC VADJ supports 1.8 V or 1.2 V (discrete values; default 1.8 V). The Z11-P uses the same Alinx base board as the Z7-P (the vendor documents them jointly as the "Z7-P/Z11-P development board" with an identical base-board feature set): the FMC_VADJ rail comes from a dedicated ETA1471 buck regulator whose feedback divider is reconfigured by 2-pin jumper J8 — open = 1.8 V, fitted = 1.2 V. The FMC IPMI EEPROM is not consulted.
