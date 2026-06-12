---
mpn: TySOM-M-MPFS250
name: TySOM-M-MPFS250
status: active
url: https://www.aldec.com/en/products/emulation/tysom_boards/polarfire_microchip/tysom_m_mpfs250
vendor: aldec
price: null
device: { part: MPFS250T-FCG1152E, vendor: microchip }
---

## Memory
- DDR4 2GB 32-bit
- DDR4 2GB 36-bit ECC

## Flash
- QSPI 128MB

## EEPROM
- data 64Kbit

## Storage
- microSD x1

## Video
- HDMI Out x1

## Networking
- 1GbE x2
- QSFP+ x1

## Serial
- CAN x1

## PCIe
- Slot Gen2 x4

## USB
- Mini-B 2.0 host

## USB UART/JTAG
- Mini-B UART

## Expansion
- FMC HPC "FMC1" VADJ 1.2-3.3V
- FMC HPC "FMC2" VADJ 1.2-3.3V
- Pmod x1

## Sensors
- Accelerometer
- Temperature

## User I/O
- LEDs x4
- DIP switches x4
- Pushbuttons x1

## Features
- Power monitoring

## Extras
- eMMC (size not published)
- USB-UART bridge is a MaxLinear XR21V1414 exposing four UART channels (HSS, Linux, OpenSBI and RISC-V consoles)
- JTAG header for FlashPro4/5 programmer
- Dedicated FMC JTAG connector with automatic FMC card detection and JTAG chain configuration
- 12V input via 6-pin PCIe power connector (60W minimum supply)

## Notes

FMC VADJ/VIOA is set per slot with DIP switches [S3] (FMC1) and [S4] (FMC2):

| Voltage | SW1 | SW2 | SW3 | SW4 |
|---|---|---|---|---|
| 1.2V | OFF | OFF | OFF | OFF |
| 1.5V | ON  | OFF | OFF | OFF |
| 1.8V | ON  | ON  | OFF | OFF |
| 2.5V | ON  | ON  | ON  | OFF |
| 3.3V | ON  | ON  | ON  | ON  |

Aldec does not document a factory-default switch position. Selecting the wrong FMC voltage can damage the board or the mezzanine card. JTAG routing to each FMC slot can be disconnected via DIP switches [S1]/[S2].
