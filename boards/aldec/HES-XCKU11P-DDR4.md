---
mpn: HES-XCKU11P-DDR4
name: HES-XCKU11P-DDR4
status: active
url: https://www.aldec.com/en/products/emulation/hes_fpga_boards/kintex_ultrascale_plus/hes_xcku11p_ddr4
vendor: aldec
price: null
device: { part: XCKU11P-3FFVE1517E, vendor: amd-xilinx }
---

## EEPROM
- data I2C 64Kbit
- data I2C 64Kbit

## Clocking
- Programmable

## PCIe
- Edge Gen3 x16
- Edge Gen4 x8

## Networking
- QSFP-DD x2

## Expansion
- FMC HPC "FMC1" VADJ 1.0-1.8V

## Sensors
- Temperature

## User I/O
- LEDs x4

## Features
- Power monitoring

## Extras
- DDR4 SO-DIMM socket for an external memory module (64-bit data plus ECC check bits)
- 512Mbit flash memory with Tandem PROM support
- Battery-backed BBRAM encryption key storage
- Combined UART/JTAG connector
- 6-pin auxiliary PCIe power connector; the board can also run from the PCIe edge connector alone in low-power configurations (without FMC and QSFP modules)
- FMC HPC site provides 160 single-ended / 80 differential I/O plus 8 transceiver links
- On-board 100MHz, 250MHz and 400MHz differential clocks plus a 200MHz DDR4 reference clock
- Low-profile half-length PCIe add-in card (1U form factor)

## Notes

FMC1 VADJ is selected manually on the board's DIP switch bank S1, whose printed selection table lists 1.0V, 1.2V, 1.35V, 1.5V and 1.8V. The same bank also sets the VIOA/VIOB I/O rails serving the FMC site; VADJ and VIOB are brought out to test points beside the connector, and S1 additionally carries the FMC_POWER_EN / FMC_POWER_ERR functions.

There is no automatic voltage negotiation: the board does not read the mezzanine's IPMI EEPROM, so S1 must be set to a voltage the card accepts before power-up. Aldec does not publish a factory-default switch position; check S1 against the board's own selection table before fitting a mezzanine, as selecting the wrong FMC voltage can damage the board or the card.
