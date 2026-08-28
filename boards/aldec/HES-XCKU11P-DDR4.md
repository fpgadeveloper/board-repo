---
mpn: HES-XCKU11P-DDR4
name: HES-XCKU11P-DDR4
status: active
url: https://www.aldec.com/en/products/emulation/hes_fpga_boards/kintex_ultrascale_plus/hes_xcku11p_ddr4
vendor: aldec
price: null
device: { part: XCKU11P-3FFVE1517E, vendor: amd-xilinx }
---

## Memory
- DDR4 8GB 72-bit ECC SODIMM

## Flash
- QSPI 64MB

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

## USB UART/JTAG
- Type-A JTAG/UART

## Expansion
- FMC HPC "FMC1" VADJ 1.0-1.8V

## Sensors
- Temperature

## User I/O
- LEDs x4

## Features
- Power monitoring

## Extras
- Configuration flash supports the Tandem PROM flow
- Battery-backed BBRAM encryption key storage
- 6-pin auxiliary PCIe power connector; the board can also run from the PCIe edge connector alone in low-power configurations (without FMC and QSFP modules)
- FMC HPC site provides 160 single-ended / 80 differential I/O plus 8 transceiver links
- On-board 100MHz, 250MHz and 400MHz differential clocks plus a 200MHz DDR4 reference clock
- Fan power header
- Low-profile half-length PCIe add-in card (1U form factor)

## Notes

### FMC1 VADJ

FMC1 VADJ is selected manually on the board's DIP switch bank S1, whose printed
selection table lists 1.0V, 1.2V, 1.35V, 1.5V and 1.8V. The factory default is
**1.8V** — all S1 switches ON — which sets both VADJ and the VIOB I/O rail
serving the FMC site. VADJ and VIOB are brought out to test points beside the
connector, and S1 additionally carries the FMC_POWER_EN / FMC_POWER_ERR
functions.

There is no automatic voltage negotiation: the board does not read the
mezzanine's IPMI EEPROM, so S1 must be set to a voltage the card accepts before
power-up. Selecting the wrong FMC voltage can damage the board or the card.

### FMC1 signal coverage

Aldec confirms that every FMC HPC signal is routed at FMC1 except the **DP8 and
DP9** transceiver pairs — matching the "8x GTY links" the product page quotes for
the site. There is no public pin listing, XDC or constraints file for the
connector, so this catalog carries no pin-level routing data for the slot and
cannot check FMC mezzanine compatibility against it automatically.

### DDR4 SO-DIMM

The SO-DIMM socket is wired 64-bit data plus 8 ECC check bits (72-bit). Boards
ship with an 8 GB DDR4-2666 module fitted; other capacities and speeds are
available on request. Aldec's published Vivado board files define 1600 and 2133
presets for the interface.

### Documentation

Aldec does not publish a user guide or technical specification for this board —
the documentation portal requires a login and full documentation is under NDA.
This entry is built from the product page, Aldec's published Vivado board files,
and details confirmed by Aldec.
