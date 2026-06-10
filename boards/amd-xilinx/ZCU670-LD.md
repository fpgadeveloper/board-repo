---
mpn: ZCU670-LD
name: ZCU670-LD
status: active
url: https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/zcu670.html
vendor: amd-xilinx
price: { value: 16995, currency: USD }
device: { part: XCZU57DR-2FSVE1156I, vendor: amd-xilinx }
---

## Memory
- DDR4 4GB 64-bit SODIMM
- DDR4 4GB 64-bit

## Networking
- 1GbE x1
- SFP28 x4

## USB
- Micro-B 3.0 host

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC+ "FMCP" VADJ 1.2-1.8V
- RFMC x2

## Storage
- microSD x1

## User I/O
- LEDs x4
- Pushbuttons x6
- DIP switches x2

## Features
- Power monitoring
- Programmable VADJ

## Notes

VADJ_FMC supports 1.2 V / 1.5 V / 1.8 V (discrete values; default 1.8 V with no FMC attached). Set at boot by the MSP430 System Controller (U38) per VITA 57.1 IPMI: it reads the FMC's I2C EEPROM and picks a voltage supported by both board and card, or 0.0 V if the EEPROM data is invalid. The System Controller user interface can override the IPMI routine with an explicit value.
