---
mpn: Papilio-Pro
name: Papilio Pro
status: discontinued
url: https://www.seeedstudio.com/Papilio-Pro-p-1301.html
vendor: gadget-factory
price: { value: 93.49, currency: USD }
device: { part: XC6SLX9-2TQG144C, vendor: amd-xilinx }
---

## Memory
- SDRAM 8MB 16-bit

## Flash
- SPI 8MB

## USB UART/JTAG
- Mini-B JTAG/UART

## Expansion
- GPIO Header x2

## User I/O
- LEDs x1

## Extras
- 48 user I/O pins (3.3V) in Papilio Wing form factor

## Notes
The dual-channel FTDI FT2232 handles both serial and programming: Channel A is an asynchronous serial UART (up to 2 MHz) and Channel B drives the FPGA JTAG pins for programming. Populating reset header JP4 holds the Spartan-6 in reset, freeing the JTAG pins so the FT2232 can act as a JTAG/SPI/MPSSE programmer.

The on-board 32 MHz oscillator feeds the FPGA Clock Management Tile (2 PLLs + 2 DCMs) and can be synthesized to other frequencies internally. The 64Mbit SPI flash supports Spartan-6 multi-boot.
