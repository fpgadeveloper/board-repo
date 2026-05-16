## Configuration

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
