---
mpn: TR5
name: TR5
status: active
url: https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1001
vendor: terasic
price: { value: 7835, currency: USD }
device: { part: 5SGXEA7N2F45C2N, vendor: altera }
---

## Memory
- DDR3 8GB SODIMM

## SRAM
- SSRAM 2MB 16-bit

## Flash
- BPI 128MB 16-bit

## Clocking
- Programmable
- SMA clock in x1
- SMA clock out x1

## PCIe
- iPass Gen3 x4

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC HPC "HPC0" VADJ 1.2-3.0V
- FMC HPC "HPC1" VADJ 1.2-3.0V
- FMC LPC "LPC0" VADJ 1.2-3.0V
- FMC LPC "LPC1" VADJ 1.2-3.0V
- GPIO Header x1

## Storage
- SATA x2

## User I/O
- LEDs x4
- Pushbuttons x4
- DIP switches x4

## Notes

Each FMC slot's VCCIO (VADJ) is jumper-selectable to 1.2 V / 1.5 V / 1.8 V / 2.5 V / 3.0 V via JP5 (FMC A), JP6 (FMC B), JP7 (FMC C) and JP9 (FMC D); default 2.5 V. Because the FMC connectors cross-connect to shared FPGA banks, 3.0 V only takes effect if all four slots are set to 3.0 V. Set jumpers before power-on — the board does not read the FMC IPMI EEPROM.
