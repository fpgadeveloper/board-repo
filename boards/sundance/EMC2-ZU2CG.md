---
mpn: EMC2-ZU2CG
name: EMC2-ZU2CG
status: active
url: https://store.sundance.com/product/emc2-zu2cg/
vendor: sundance
price: { value: 1395, currency: GBP }
device: { part: XCZU2CG-1SFVC784I, vendor: amd-xilinx }
---

## Memory
- DDR4 2GB 32-bit

## Flash
- QSPI 64MB
- QSPI 64MB
- eMMC 8GB

## EEPROM
- MAC

## Clocking
- Programmable

## PCIe
- PCIe/104 Gen2 x4

## Video
- HDMI Out x1

## Networking
- 1GbE x1

## Serial
- RS-232 x1

## Expansion
- FMC LPC "LPC" VADJ 1.8-3.3V

## Storage
- SATA x1
- microSD x1

## Notes

FMC VADJ is jumper-selectable between 1.8 V, 2.5 V and 3.3 V (discrete values): the FMC connector's VADJ pins are tied to the SoM's FPGA I/O bank rail (VCCIO), and jumper JP8 (with JP8A) selects that rail's voltage — position 1-2 for 3.3 V, 2-3 for 1.8 V, 2-JP8A for 2.5 V. Set the jumper before power-on; the board does not read the FMC IPMI EEPROM. Caution: HP FPGA banks only support up to 1.8 V — the safe setting depends on the fitted SoM, and Sundance may ship the board with only the 1.8 V selection populated.
