---
mpn: MPFS-DISCO-KIT
name: PolarFire SoC Discovery Kit
status: active
url: https://www.microchip.com/en-us/development-tool/mpfs-disco-kit
vendor: microchip
price: { value: 132, currency: USD }
device: { part: MPFS095T-1FCSG325E, vendor: microchip }
---

## Memory
- DDR4 1GB 16-bit

## Video
- MIPI CSI x1

## Networking
- 1GbE x1

## USB UART/JTAG
- Type-C JTAG/UART

## Expansion
- Raspberry Pi x1
- Click x1

## Storage
- microSD x1

## User I/O
- LEDs x8
- Pushbuttons x2
- DIP switches x8

## Extras
- On-board Embedded FlashPro5 (eFP5) programmer/debugger — no external programming hardware required
- FT4232HL USB-to-quad-UART bridge exposing three UART channels
- 10-pin connector (J48) for an external serial 8-digit 7-segment display board
- Debug live-probe header (J12)
- 50 MHz single-ended oscillator (fabric) and 125 MHz LVDS oscillator (MSS reference clock)
- Powered from the USB Type-C port (5V/3A) or a 5V DC jack, selected by jumper J47
- Board size approximately 4.15 x 3.3 inches

## Notes

The DDR4 device is a Micron MT40A512M16TB-062E (1 GB, x16) on MSS bank 6. Ethernet
uses a Microchip VSC8221 10/100/1000BASE-T PHY connected over SGMII on MSS bank 5.
The Raspberry Pi MIPI RX connector (J11) is on the underside of the board, as is the
microSD socket.

Default jumper settings:

| Jumper | Purpose | Default |
|---|---|---|
| J45 | Bank 1 / Bank 5 I/O voltage (VDDI1_5): pins 1-2 = 3.3V (Raspberry Pi GPIO and mikroBUS), pins 2-3 = 2.5V (MIPI RX and Ethernet) | 1 and 2 closed |
| J46 | VDDAUX1 voltage: pins 1-2 = 3.3V, pins 2-3 = 2.5V | 1 and 2 closed |
| J47 | Power source: pins 1-2 closed = USB Type-C (J4), pins 1-2 open = 5V DC jack (J7) | 1 and 2 closed |
| J49 | 7-segment display connector voltage: pins 1-2 = 3.3V, pins 2-3 = 5V | 2 and 3 closed |

If VDDI1_5 is set to 2.5V (J45 pins 2-3 closed), VDDAUX1 must also be set to 2.5V
(J46 pins 2-3 closed).

Source: PolarFire SoC FPGA Discovery Kit User Guide (DS50003630E).
