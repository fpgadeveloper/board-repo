---
mpn: HEA13-Carrier
name: HEA13 Base Board
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Virtex-UltraScale-plus/HEA13.html
vendor: alinx
price: null
---

## Clocking
- SMA clock in x2

## M.2
- M-key
- E-key

## Video
- DisplayPort x1

## Networking
- 1GbE x1
- 5GbE x1 RJ45-only
- 10GbE x1 RJ45-only
- QSFP28 x4

## USB
- Type-C 3.2 OTG x2

## USB UART/JTAG
- Type-C UART

## Expansion
- FMC+ "FMCP0" VADJ 1.8V
- FMC+ "FMCP1" VADJ 1.8V
- GPIO Header x1

## Storage
- microSD x2

## User I/O
- LEDs x3
- Pushbuttons x3

## Notes

VADJ is fixed at 1.8 V on both FMC+ sites — the user guide states the FMC I/O level standard is 1.8 V (FMC1+ on banks 69/70/71, FMC2+ on the other HP banks of the VU13P, which only supports up to 1.8 V VCCO). No jumper, programmable regulator, or FMC EEPROM auto-negotiation is documented; the on-board MCU only sequences power for the Jetson AGX site.
