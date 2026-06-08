---
mpn: AXE5-Falcon
name: AXE5-Falcon
status: active
url: https://github.com/ArrowElectronics/Agilex-5/wiki/Agilex-5-E-Series-AXE5-Falcon-Development-Platform
vendor: arrow
price: null
device: { part: A5EE013BB23BE6SCS, vendor: altera }
---

## Memory
- DDR4 2GB 32-bit

## Flash
- QSPI 32MB

## EEPROM
- MAC I2C 2Kbit 24AA025E48T
- data I2C 128Kbit 24AA128T

## Clocking
- Programmable

## Video
- HDMI Out x1
- MIPI CSI x2

## Networking
- 1GbE x1

## USB
- Type-A 2.0 host x4

## USB UART/JTAG
- Type-C JTAG/UART

## Expansion
- Pmod x1
- CRUVI HS x3
- CRUVI LS x1
- Raspberry Pi x1

## Storage
- microSD x1

## User I/O
- LEDs x2
- RGB LEDs x4
- Pushbuttons x6
- DIP switches x6

## Extras
- Programmable fan controller with FPGA temperature-diode monitoring (MAX31760)
- 4-pin I2C1 header
- 4-pin I3C0 header
- On-board USB Blaster III for FPGA configuration (shares the USB-C connector)

## Notes

Powered from either the 5 V DC barrel jack (J6) or the USB-C connector (J25); the
board selects the active source automatically.

FPGA configuration is supported over JTAG (on-board USB Blaster III via the USB-C
connector) or via Active Serial boot from the on-board QSPI flash.
