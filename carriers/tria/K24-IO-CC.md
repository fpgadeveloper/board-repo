---
mpn: K24-IO-CC
name: K24 IO Carrier Card
status: eol
url: https://www.tria-technologies.com/products/k24-development-kit/
vendor: tria
price: null
---

## EEPROM
- MAC+UID I2C 2Kbit AT24MAC402

## Networking
- 1GbE x1

## USB
- Type-A 2.0 host

## USB UART/JTAG
- Type-C JTAG/UART

## Expansion
- Pmod x1
- Click x2

## Storage
- microSD x1

## User I/O
- LEDs x6
- RGB LEDs x2
- Pushbuttons x4
- DIP switches x4

## Extras
- HSIO TXR2 expansion sites x2 — Samtec QSH-020 high-speed connectors carrying PL I/O and PS GTR transceivers
- USB Type-C 15V power input connector

## Notes

The carrier card carries the Kria K24 SOM on a 240-pin connector (CON1). It provides
10/100/1000 Ethernet (Microchip KSZ9131RNXI PHY), a USB 2.0 Type-A host port
(USB3321C PHY), a shared USB Type-C JTAG/UART debug port, microSD, two HSIO TXR2
high-speed expansion sites, two MikroE Click sites, and a Type 1A Pmod site.

MPSoC boot mode is selected with the Boot Mode Switch SW1 (default M[3:0] = 0010,
Master SPI flash):

| Boot mode | M[3:0] | SW1 (1-2-3-4) |
|---|---|---|
| Master SPI flash | 0010 | ON-ON-OFF-ON |
| microSD card | 0101 | ON-OFF-ON-OFF |
| JTAG | 0000 | ON-ON-ON-ON |
