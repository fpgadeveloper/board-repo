---
mpn: FMC-SpaceWire-SpaceFibre-Mk3
name: FMC SpaceWire/SpaceFibre Board Mk3
status: active
url: https://www.star-dundee.com/products/fmc-spacewire-spacefibre-board/
vendor: star-dundee
price: null
connector_type: hpc
vadj_min: 1.8
vadj_max: 3.3
---

## EEPROM
- ID I2C 2Kbit

## Clocking
- SMA clock in x2

## User I/O
- RGB LEDs x12
- LEDs x1

## Features
- Power monitoring

## Extras
- 4x SpaceWire ports — 9-pin micro-miniature D-type connectors, compliant to ECSS-E50-12A / ECSS-E-ST-50-12C / Rev.1, max 300 Mbit/s, via standard LVDS buffers (16 LVDS differential pairs to the FMC connector)
- 2x SpaceFibre ports — Type-C EGSE electrical connectors, compliant to ECSS-E-ST-50-11C, 1.88-3.2 Gbit/s, AC-coupled (2 gigabit-transceiver differential pairs)
- Partially populated HPC FMC card implementing ANSI/VITA 57.1 (compatible with LPC, HPC and FMC+ carrier slots)
- Two GBTCLK LVDS clock outputs to the carrier (GBTCLK0/GBTCLK1) sourced from a selectable on-board 125MHz or 156.25MHz oscillator or the external SMA input
- 20x GPIO pins across two 10-pin headers (J5/J9) for breakout and test
- Two 4x4 LVDS switch banks (SW1/SW2) to swap SpaceWire input pairs between paired ports for carrier pinout flexibility
- Tri-colour port status LEDs programmable over the FMC I2C bus
