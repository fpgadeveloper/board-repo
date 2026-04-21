## Configuration

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
