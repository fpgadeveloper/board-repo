---
mpn: AXKU040
name: AXKU040
status: active
url: https://www.en.alinx.com/Product/FPGA-Development-Boards/Kintex-UltraScale/AXKU040.html
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

## Video
- HDMI Out x1

## Networking
- 1GbE x2
- SFP+ x4

## Serial
- CAN x1

## USB UART/JTAG
- Micro-B UART

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- FMC LPC "LPC0" VADJ 1.8V
- FMC LPC "LPC1" VADJ 1.2-3.3V

## Features
- Programmable VADJ

## Storage
- SATA x2
- microSD x1

## User I/O
- LEDs x4
- Pushbuttons x2

## Notes

FMC supply differs per slot: the HPC (banks 66-68) and LPC "FMC1" = LPC0 (banks 47/48) are fixed at 1.8 V ("cannot be modified"). Only LPC "FMC2" = LPC1 (HR banks 64/65, rail FMC2_VADJ) is adjustable — default 1.8 V, changed by software reprogramming the LP873220 PMIC; there is no System Controller and the board does not read the FMC IPMI EEPROM. Its 1.2-3.3 V range is inferred from the HR-bank VCCO options (1.2/1.35/1.5/1.8/2.5/3.3 V), not enumerated by the manual.
