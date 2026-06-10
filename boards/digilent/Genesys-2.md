---
mpn: Genesys-2
name: Genesys-2
status: active
url: https://digilent.com/shop/genesys-2-kintex-7-fpga-development-board/
vendor: digilent
price: { value: 1099, currency: USD }
device: { part: XC7K325T-2FFG900C, vendor: amd-xilinx }
---

## Memory
- DDR3 1GB 32-bit

## Audio
- Codec ADAU1761
- Line in x1
- Line out x1
- Headphone x1
- Microphone x1

## Video
- HDMI In x1
- HDMI Out x1
- DisplayPort x2
- VGA Out x1

## Display
- OLED 128x32

## Networking
- 1GbE x1

## USB
- Micro-B 2.0 OTG
- Type-A 2.0 host

## USB UART/JTAG
- Micro-B JTAG
- Micro-B UART

## Expansion
- FMC HPC "HPC" VADJ 1.2-3.3V
- Pmod x5
- XADC Header x1

## Storage
- microSD x1

## User I/O
- LEDs x8
- Pushbuttons x5
- DIP switches x8

## Notes

VADJ supports 1.2 V / 1.8 V / 2.5 V / 3.3 V, selected by jumper JP6 on the regulator's feedback divider (change only with power off); with JP6 unset the rail defaults to 1.2 V, and the provided master XDC/UCF files assume 1.2 V. The board does not read the FMC IPMI EEPROM — the rail also powers the user push-buttons, switches, XADC Pmod, and FPGA banks 15-17.
