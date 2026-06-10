---
mpn: DK-SOC-10AS066S-E
name: Arria 10 SX SoC Development Kit
status: active
url: https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit
vendor: altera
price: { value: 4495, currency: USD }
device: { part: 10AS066N3F40E2SG, vendor: altera }
---

## Memory
- DDR4 1GB
- DDR4 2GB

## Flash
- QSPI 128MB
- NAND 128MB

## Clocking
- Programmable

## PCIe
- Edge Gen3 x8

## Video
- DisplayPort x1

## Networking
- 1GbE x3
- SFP+ x2

## USB UART/JTAG
- Micro-B JTAG

## Expansion
- FMC HPC "FMCA" VADJ 1.1-1.8V
- FMC LPC "FMCB" VADJ 1.1-1.8V

## Storage
- microSD x1

## Notes

Each FMC slot's VADJ is jumper-selected before power-on (default 1.8 V on both slots). J42 sets FMCA VADJ to 1.1 / 1.2 / 1.35 / 1.5 / 1.8 V; J32 sets FMCB VADJ to 1.2 / 1.25 / 1.35 / 1.5 / 1.8 V (1.1 V with no jumper fitted). The board does not read the FMC IPMI EEPROM — VADJ is fixed by the jumper setting.
