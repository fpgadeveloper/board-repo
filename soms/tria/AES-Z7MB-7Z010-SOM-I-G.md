---
mpn: AES-Z7MB-7Z010-SOM-I-G
name: MicroZed-7010
status: active
url: https://www.tria-technologies.com/product/microzed/
vendor: tria
price: { value: 289, currency: USD }
device: { part: XC7Z010-1CLG400I, vendor: amd-xilinx }
---

## Memory
- DDR3 1GB 32-bit

## Flash
- QSPI 16MB

## Networking
- 1GbE x1

## USB
- Type-A 2.0 OTG

## USB UART/JTAG
- Micro-B UART

## Expansion
- Pmod x1

## Storage
- microSD x1

## Notes

### Configuration

Boot mode is determined by jumper headers labelled JP3, JP2 and JP1.

| Boot mode          | JP3 | JP2 | JP1 |
|--------------------|---|---|---|
| JTAG (cascaded)    | 0 | 0 | 0 |
| JTAG (independent) | 0 | 0 | 1 |
| Quad-SPI           | 1 | 0 | X |
| SD Card            | 1 | 1 | X |

Notes:

* 0 = install jumper between pins 1 and 2
* 1 = install jumper between pins 2 and 3
* X = don't care
