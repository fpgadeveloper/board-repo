---
mpn: NetFPGA-SUME
name: NetFPGA-SUME
status: discontinued
url: https://netfpga.org/NetFPGA-SUME.html
vendor: digilent
price: null
device: { part: XC7VX690T-3FFG1761C, vendor: amd-xilinx }
---

## Memory
- DDR3 4GB SODIMM
- DDR3 4GB SODIMM
- QDR-II+ 9MB 36-bit
- QDR-II+ 9MB 36-bit
- QDR-II+ 9MB 36-bit

## Flash
- SPI 64MB
- SPI 64MB

## PCIe
- Edge Gen3 x8

## Networking
- SFP+ x4

## Expansion
- FMC HPC "HPC" VADJ 1.8V
- Pmod x1

## Storage
- SATA x2
- microSD x1

## Features
- Power monitoring

## Extras
- Samtec QTH-DP high-speed connector exposing 8 serial links (additional GTH transceivers)
- On-board clock recovery circuit

## Notes

VADJ is fixed at 1.8 V — the FMC VADJ pins are tied directly to the board's VCC1V8 rail, and all FPGA I/O routed to the FMC connector supports 1.8 V logic only. There is no jumper or programmable regulator for VADJ; FMC modules requiring a different VADJ voltage are electrically incompatible.
