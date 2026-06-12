---
mpn: AXKU041
name: AXKU041
status: active
url: https://www.en.alinx.com/detail/275
vendor: alinx
price: { value: 1053.99, currency: GBP }
device: { part: XCKU040-2FFVA1156I, vendor: amd-xilinx }
---

## Memory
- DDR4 4GB 64-bit

## Flash
- QSPI 32MB
- QSPI 32MB

## EEPROM
- data I2C 4Kbit 24LC04

## Sensors
- Temperature LM75A

## PCIe
- Edge Gen3 x8

## Networking
- 1GbE x1
- SFP+ x2

## Serial
- CAN x1

## USB UART/JTAG
- Micro-B UART

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- FMC LPC "LPC0" VADJ 1.8V
- FMC LPC "LPC1" VADJ 1.8V

## Storage
- microSD x1

## User I/O
- LEDs x4
- Pushbuttons x1

## Notes

All three FMC slots run at a fixed 1.8 V IO level: the user manual states the LPC FMC1 (banks 47/48) and LPC FMC2 (banks 64/65) levels are "1.8V and cannot be modified", and the HPC (banks 66-68) voltage standard is 1.8 V. No jumper or programming mechanism exists.
