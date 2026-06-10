---
mpn: LAV-E70-EVN
name: Avant-E Evaluation
status: active
url: https://www.latticesemi.com/products/developmentboardsandkits/avant-e-evaluation-board
vendor: lattice
price: { value: 300, currency: USD }
device: { part: LAV-AT-E70-2LFG1156C, vendor: lattice }
---

## Memory
- LPDDR4 2GB 32-bit

## Flash
- SPI 64MB

## USB UART/JTAG
- Mini-B JTAG

## Expansion
- FMC HPC "FMC1" VADJ 1.5-3.3V
- FMC HPC "FMC2" VADJ 1.5-3.3V
- Pmod x3
- Raspberry Pi x1

## User I/O
- LEDs x16
- Pushbuttons x4
- DIP switches x8
- 7-segment displays x3

## Notes

Each FMC slot has its own VADJ rail (VFMC1_ADJ / VFMC2_ADJ), jumper-selectable to 1.5 V (no jumper), 1.8 V (default), 2.5 V, or 3.3 V — FMC1 via JP7/JP8/JP43, FMC2 via JP44/JP45/JP46. Voltage is set before power-on; the board does not read the FMC IPMI EEPROM. FPGA banks 3/4/5 (FMC1) and 7/8/9 (FMC2) can optionally be powered from the corresponding VADJ rail via jumpers, and bank 5 is shared between the two slots — keep its signals at one voltage when both FMCs are used.
