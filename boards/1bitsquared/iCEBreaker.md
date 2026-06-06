---
mpn: iCEBreaker
name: iCEBreaker
status: active
url: https://1bitsquared.com/products/icebreaker
vendor: 1bitsquared
price: { value: 79.95, currency: USD }
device: { part: iCE40UP5K-SG48I, vendor: lattice }
---

## Memory
- PSRAM 8MB

## Flash
- QSPI 16MB

## USB UART/JTAG
- Type-C JTAG/UART

## Expansion
- Pmod x3

## User I/O
- LEDs x7
- RGB LEDs x1
- Pushbuttons x4

## Extras
- Fully open-source FPGA flow (Yosys / nextpnr / IceStorm / Icarus Verilog / Amaranth HDL); also usable with Lattice vendor tools
- FT2232H USB bridge (JTAG configuration + UART) over the USB-C connector
- Dedicated CRESET configuration-reset button
- Snap-off breakout section (iCEstick-like): 5 LEDs + 3 push buttons, convertible to Pmod host / Pmod device
- FTDI Async FIFO mode support via unpopulated zero-ohm resistors (shares snap-off section pins)
- Direct SRAM programming option via FTDI (solder jumpers)
- Debug header exposing all 6 QSPI pins; supply-rail header (5V / 3V3 / 1V2 / GND)
- Current-measurement jumpers / zero-ohm resistors on all power rails
- Length-matched Pmod IO signals
- Ships with unpopulated Pmod connectors: 3x host Pmod + 1x device Pmod

## Notes

V1.1a hardware. Changes from V1.0: USB-C connector (replacing micro-USB), populated "ears"
(with the ear-board connectors included), RGB LED mounted by default, 64 Mbit (8 MB) QSPI
PSRAM mounted by default, a dedicated CRESET button, and length-matched Pmod IO.

FPGA: Lattice iCE40 UltraPlus 5K in a QFN48 (SG48) package — 5280 logic cells, 128 Kbit
dual-port block RAM, 1 Mbit single-port RAM, 8 DSPs, PLL, two SPI + two I2C hard IP blocks.

User I/O counts include the snap-off section. Main section: 2 user LEDs + RGB LED + 1 user
button. Snap-off section: 5 LEDs + 3 push buttons. The CRESET button and the Power / CDONE
status LEDs are not counted as user I/O.

Configuration flash is a Winbond W25Q128JVSIM (128 Mbit / 16 MB, QSPI-DDR capable). The
FT2232H bridge shares a 12 MHz crystal with the FPGA.

Expansion: one "double" Pmod (two 8-signal Pmod connectors, PMOD1A + PMOD1B) plus one
single Pmod on the snap-off section (PMOD2) — three Pmod connectors total.
