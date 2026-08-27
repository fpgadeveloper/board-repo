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
- Micro-B JTAG

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

### Memory configurations

Aldec offers the board in two memory builds under the same product name, with no
separate ordering code:

- **432 Mb QDR-II+** — three 144 Mb QDR-II+ SRAMs (the configuration listed above)
- **144 Mb QDR-II+ with 32 Gb DDR4** — one 144 Mb QDR-II+ SRAM plus two 16 Gb
  32-bit DDR4 devices

This entry lists the three-QDR-II+ build, which is the configuration described by
Aldec's published Vivado board definition files
([github.com/Aldecinc/HES](https://github.com/Aldecinc/HES)); those files also
give the 18-bit width of each QDR-II+ interface. Check with Aldec which build a
given board carries.

### FPGA speed grade

The product page names the FPGA as XCVU9P-FLGB2104 without a speed grade. Aldec
publishes Vivado board definitions for two board revisions — 1.5-2-E and 1.5-3-E
— carrying `XCVU9P-2FLGB2104E` and `XCVU9P-3FLGB2104E` respectively. This entry
lists the -2 speed grade; confirm the grade of a specific unit with Aldec.

### Board naming

The board silkscreen carries Aldec's earlier HES-HPC-HFT name for this hardware.
HES-XCVU9P-QDR is the current product name.
