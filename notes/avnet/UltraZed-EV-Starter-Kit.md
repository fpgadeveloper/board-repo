## Configuration

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
