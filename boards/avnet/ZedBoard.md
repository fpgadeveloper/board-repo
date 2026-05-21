---
mpn: ZedBoard
name: ZedBoard
status: active
url: https://www.avnet.com/americas/products/avnet-boards/avnet-board-families/zedboard/
vendor: avnet
price: { value: 499, currency: USD }
device: { part: XC7Z020-1CLG484C, vendor: amd-xilinx }
---

## Memory
- DDR3 512MB

## Flash
- QSPI 32MB

## Audio
- Codec ADAU1761
- Line in x1
- Line out x1
- Headphone x1
- Microphone x1

## Video
- HDMI Out x1
- VGA Out x1

## Display
- OLED 128x32

## Networking
- 1GbE x1

## USB
- Micro-B 2.0 OTG

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC LPC "LPC"
- Pmod x5
- XADC Header x1

## Storage
- SD x1

## User I/O
- Pushbuttons x7
- DIP switches x8

## Notes

### Configuration

Boot mode is determined by jumper headers labelled MIO2-MIO6.

| Boot mode          | MIO6 | MIO5 | MIO4 | MIO3 | MIO2 |
|--------------------|---|---|---|---|---|
| JTAG (cascaded)    | X | 0 | 0 | 0 | 0 |
| JTAG (independent) | X | 0 | 0 | 0 | 1 |
| Quad-SPI           | X | 1 | 0 | 0 | X |
| SD Card            | X | 1 | 1 | 0 | X |

Notes:

* 0 = install jumper between middle pin and GND
* 1 = install jumper between middle pin and 3V3
* X = don't care
* MIO6 determines PLL used (0) or bypassed (1)
