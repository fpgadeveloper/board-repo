---
mpn: MPF300-VIDEO-KIT
name: PolarFire Video
status: active
url: https://www.microchip.com/en-us/development-tool/mpf300-video-kit-ns
vendor: microchip
price: { value: 1302, currency: USD }
device: { part: MPF300T-1FCG1152E, vendor: microchip }
---

## Memory
- DDR4 4GB 32-bit

## Flash
- SPI 128MB

## Video
- HDMI In x1
- HDMI Out x2
- MIPI DSI x1
- MIPI CSI x2

## USB UART/JTAG
- Mini-B JTAG/UART

## Expansion
- FMC HPC "HPC" VADJ 1.2-3.3V

## Notes

VADJ (`VCCIO_HPC_VADJ`, FPGA bank 4) is jumper-selectable via J25: 3.3 / 2.5 / 1.8 / 1.5 / 1.2 V (default 1.8 V, pins 5-6 closed). Set the jumper before power-on — the board does not read the FMC card's IPMI EEPROM.
