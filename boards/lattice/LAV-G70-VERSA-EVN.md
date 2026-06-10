---
mpn: LAV-G70-VERSA-EVN
name: Avant-G Versa
status: active
url: https://www.latticesemi.com/products/developmentboardsandkits/avant-g-versa-board
vendor: lattice
price: { value: 2447, currency: USD }
device: { part: LAV-AT-G70-3LFG1156C, vendor: lattice }
---

## PCIe
- Edge Gen3 x4

## Networking
- SFP28 x2
- QSFP28 x1

## Expansion
- FMC+ "FMC+" VADJ 1.2-1.8V
- Pmod x2
- Raspberry Pi x1

## Notes

VCC_VADJ for the FMC+ connector (J19) supports 1.2 V / 1.35 V / 1.5 V / 1.8 V (default 1.8 V). The voltage is set by changing feedback resistor R130 on the MPM3683-7 regulator (1 kΩ = 1.8 V, 1.33 kΩ = 1.5 V, 1.6 kΩ = 1.35 V, 2 kΩ = 1.2 V) — a soldered resistor, not a jumper, and the board does not read the FMC IPMI EEPROM.
