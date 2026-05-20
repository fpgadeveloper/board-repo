---
mpn: UltraZed-EV-Starter-Kit
name: UltraZed-EV Starter Kit
status: discontinued
url: https://www.xilinx.com/products/boards-and-kits/1-y3n9v1.html
vendor: tria
price: { value: 1595, currency: USD }
composition: { som: AES-ZU7EV-1-SOM-I-G, carrier: AES-ZU7EV-1-CC-FMC-G }
---

## Notes

### Configuration

Boot mode is determined by DIP switch labelled SW2.

| Boot mode          | 1 | 2 | 3 | 4 |
|--------------------|---|---|---|---|
| JTAG               | 1 | 1 | 1 | 1 |
| Quad-SPI24         | 0 | 1 | 1 | 1 |
| Quad-SPI32         | 1 | 0 | 1 | 1 |
| SD1/MMC33          | 0 | 1 | 0 | 1 |
| SD1/MMC33          | 1 | 0 | 0 | 0 |
| EMMC18             | 1 | 0 | 0 | 1 |

Notes:

* 0 = OFF
* 1 = ON
* JTAG and SD card interfaces are only accessed on the carrier card
