---
mpn: MPF300-SPLASH-KIT
name: PolarFire Splash
status: active
url: https://www.microchip.com/en-us/development-tool/mpf300-splash-kit
vendor: microchip
price: { value: 349, currency: USD }
device: { part: MPF300T-1FCG484E, vendor: microchip }
---

## Flash
- SPI 128MB

## PCIe
- Edge Gen2 x4

## Networking
- 1GbE x1

## USB UART/JTAG
- Mini-B JTAG/UART

## Expansion
- FMC LPC "LPC" VADJ 1.2-3.3V

## Features
- Power monitoring

## Notes

VADJ (`VCCIO_LPC_VADJ`, FPGA bank 2, FMC connector J17) is jumper-selectable via J32: 3.3 / 2.5 / 1.8 / 1.5 / 1.2 V (default 3.3 V, pins 1-2 closed). Set the jumper before power-on — the board does not read the FMC card's IPMI EEPROM.
