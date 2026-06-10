---
mpn: Nexys-Video
name: Nexys-Video
status: active
url: https://digilent.com/shop/nexys-video-artix-7-fpga-trainer-board-for-multimedia-applications/
vendor: digilent
price: { value: 549, currency: USD }
device: { part: XC7A200T-1SBG484C, vendor: amd-xilinx }
---

## Memory
- DDR3 512MB

## Flash
- QSPI 32MB

## EEPROM
- data

## Audio
- Codec ADAU1761
- Line in x1
- Line out x1
- Headphone x1
- Microphone x1

## Video
- HDMI In x1
- HDMI Out x1
- DisplayPort x1

## Display
- OLED 128x32

## Networking
- 1GbE x1

## USB
- Type-A 2.0 host

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC LPC "LPC" VADJ 1.2-3.3V
- Pmod x4
- XADC Header x1

## Storage
- microSD x1

## User I/O
- LEDs x8
- Pushbuttons x5
- DIP switches x8

## Features
- Programmable VADJ

## Notes

VADJ supports 1.2 V / 1.8 V / 2.5 V / 3.3 V (discrete values; default 1.2 V, set by on-board pull resistors that also enable the regulator at power-on). The FPGA design selects the voltage by driving the ADP2384 regulator's feedback multiplexer via the SET_VADJ(1:0) and VADJ_EN pins — the board does not read the FMC IPMI EEPROM automatically; voltages other than 1.2 V are the user design's responsibility. The same VADJ rail also powers the user pushbuttons, slide switches, XADC Pmod and FPGA banks 15/16.
