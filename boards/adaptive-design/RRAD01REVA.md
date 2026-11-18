---
mpn: RRAD01REVA
name: Spartan7 Retro Computer Board
status: active
url: https://www.adaptivedesign.ie/product-page/spartan7-retro-computer-board
vendor: adaptive-design
price: { value: 99, currency: EUR }
device: { part: XC7S25-1FTGB196C, vendor: amd-xilinx }
---

## Video
- VGA Out x1
- HDMI Out x1

## USB
- Type-A 1.1 host x4

## USB UART/JTAG
- Micro-B JTAG
- Micro-B UART

## Expansion
- Pmod x4

## User I/O
- LEDs x8
- Pushbuttons x4
- DIP switches x4

## Extras
- SPI configuration flash (capacity not stated by the vendor)
- 100MHz and 12MHz oscillators
- VGA output is 12-bit RGB (4 bits per colour) on a DB15 connector
- HDMI connector carries DVI (TMDS) driven directly from FPGA pins; vendor limits it to 1024x768
- USB host ports are low speed only (1.5Mbit/s), wired directly to FPGA pins with per-port VBUS enables; intended for keyboards and game controllers
- PROG pushbutton clears the FPGA configuration
- 12V DC jack power input (12V/1A supply sold separately)

## Notes

Also known as the "RR Retro v1.0" (the name used by the vendor's Vivado board files; silkscreen "RR V1.0 Rev A").

**Configuration mode.** A 3-position DIP switch (M0/M1/M2) selects the configuration mode; the positions are printed in a small table on the silkscreen. The board ships set to SPI flash mode with a factory test image (VGA/DVI colour bars, LED and USB gamepad tests) that starts at power-up. Switch to JTAG mode for normal development; the SPI flash can be reprogrammed from Vivado over the on-board USB-JTAG interface.

| Mode | M0 | M1 | M2 |
|---|---|---|---|
| JTAG | 1 | 0 | 1 |
| SPI flash | 1 | 0 | 0 |

**Pmod I/O voltage.** The four Pmod connectors are on FPGA bank 34, whose I/O voltage is selected between 3.3V and 2.5V by jumper J13 (2.5V allows the pins to be used as LVDS pairs). Bank 14 is fixed at 3.3V.

**Not included.** Micro-USB cables and the 12V power supply are not supplied with the board.
