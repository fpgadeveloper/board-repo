---
mpn: HES-XCVU9P-QDR
name: HES-XCVU9P-QDR
status: active
url: https://www.aldec.com/en/products/emulation/hes_fpga_boards/virtex_ultrascale_plus/hes_xcvu9p_qdr
vendor: aldec
price: null
device: { part: XCVU9P-2FLGB2104E, vendor: amd-xilinx }
---

## Memory
- QDR-II+ 18MB 18-bit
- QDR-II+ 18MB 18-bit
- QDR-II+ 18MB 18-bit

## Flash
- QSPI 64MB
- QSPI 64MB

## EEPROM
- data I2C 64Kbit 24AA64T-I/MNY
- data I2C 64Kbit 24AA64T-I/MNY

## Clocking
- Programmable

## PCIe
- Edge Gen3 x16

## Networking
- QSFP28 x2

## USB UART/JTAG
- Mini-B JTAG

## Sensors
- Temperature SI7055-A20-IM

## Features
- Power monitoring

## Extras
- Low-profile half-length PCIe add-in card with a 6-pin auxiliary PCIe power connector
- PCIe x16 Gen3 endpoint supports Tandem Reconfiguration
- Each QSFP28 cage supports a 100Gb Ethernet connection
- General-purpose 100MHz, 200MHz, 300MHz and 400MHz oscillators for the FPGA
- Three dedicated 200MHz oscillators with buffers for the QDR-II+ memories
- Dedicated clock generator for the PCIe interface
- Up to two I2C-programmable oscillators for the QSFP28 interfaces
- I2C current monitor (INA219) sharing the main I2C bus with the EEPROMs and the temperature sensor

## Notes

### Memory configuration

This entry documents the standard 432 Mb QDR-II+ build — three 144 Mb QDR-II+
SRAMs, the configuration described by Aldec's published Vivado board definition
files ([github.com/Aldecinc/HES](https://github.com/Aldecinc/HES)), which also
give the 18-bit width of each QDR-II+ interface.

Aldec's product page also describes a 144 Mb QDR-II+ plus 32 Gb DDR4 build
(two 16 Gb devices). Aldec confirms that is a separate product with its own
ordering code, not a build option of HES-XCVU9P-QDR; it is not covered by this
entry.

### FPGA speed grade

The product page names the FPGA as XCVU9P-FLGB2104 without a speed grade. Aldec
publishes Vivado board definitions for two board revisions — 1.5-2-E and 1.5-3-E
— carrying `XCVU9P-2FLGB2104E` and `XCVU9P-3FLGB2104E` respectively, and
confirms both speed grades are orderable. This entry lists the -2 grade; specify
the grade you need when ordering.

### Board naming

**HES-XCVU9P-QDR** is the official product name and orderable part number.
Boards silkscreened **HES-HPC-HFT** carry Aldec's earlier internal technical
name for the same hardware, since superseded.

### USB-JTAG

The board carries an on-board JTAG module; programming needs only a USB Mini-B
cable, with no external programming pod.

### Documentation

Aldec does not publish a user guide or technical specification for this board —
the documentation portal requires a login and full documentation is under NDA.
This entry is built from the product page, Aldec's published Vivado board files,
and details confirmed by Aldec.
