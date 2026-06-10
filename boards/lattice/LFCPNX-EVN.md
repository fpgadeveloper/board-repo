---
mpn: LFCPNX-EVN
name: LFCPNX-EVN
status: active
url: https://www.latticesemi.com/products/developmentboardsandkits/certuspro-nxevaluationboard
vendor: lattice
price: { value: 200, currency: USD }
device: { part: LFCPNX-100-9LFG672C, vendor: lattice }
---

## Flash
- SPI 16MB

## USB UART/JTAG
- Mini-B JTAG/I2C

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- Pmod x3
- Raspberry Pi x1
- GPIO Header x1

## User I/O
- LEDs x24
- Pushbuttons x4
- DIP switches x8

## Notes

VADJ (VCC_ADJ) is fixed at 1.8 V, set by the feedback divider (R242/R243) of the on-board regulator U26 (Ricoh R1273L031A). Changing it requires board rework (replace R243), and the rail must not exceed 1.8 V because it also supplies FPGA banks 3-5. There is no jumper selection and the board does not read the FMC IPMI EEPROM.
