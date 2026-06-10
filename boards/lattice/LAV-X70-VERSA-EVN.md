---
mpn: LAV-X70-VERSA-EVN
name: Avant-X Versa
status: active
url: https://www.latticesemi.com/products/developmentboardsandkits/avant-x-versa-board
vendor: lattice
price: { value: 2000, currency: USD }
device: { part: LAV-AT-X70-3LFG1156C, vendor: lattice }
---

## Flash
- OSPI 64MB

## PCIe
- Edge Gen3 x4

## Networking
- SFP28 x2
- QSFP28 x1

## Expansion
- FMC+ "FMC+" VADJ 1.2-1.8V
- Pmod x2

## Notes

VADJ (VCC_VADJ) supports 1.2 V / 1.35 V / 1.5 V / 1.8 V (discrete values; default 1.8 V, 3.3 V not supported). Selected in hardware by the fitted feedback resistor R130 on the MPM3683-7 regulator (1 k = 1.8 V, 1.33 k = 1.5 V, 1.6 k = 1.35 V, 2 k = 1.2 V) — changing it requires rework. The board does not read the FMC IPMI EEPROM to set VADJ.
