---
mpn: ADRV9009-ZU11EG
name: ADRV9009-ZU11EG RF-SOM
status: active
url: https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv9009-zu11eg.html
vendor: analog-devices
price: null
device: { part: XCZU11EG-1FFVC1760I, vendor: amd-xilinx }
---

## Memory
- DDR4 4GB 72-bit ECC
- DDR4 2GB 32-bit
- DDR4 2GB 32-bit

## Flash
- QSPI 128MB

## Analog
- RF ADRV9009 2ch 75-6000MHz
- RF ADRV9009 2ch 75-6000MHz

## Networking
- 1GbE x1 PHY-only

## USB
- PHY 2.0 OTG

## Storage
- microSD x1

## Extras
- HMC7044B high-performance jitter attenuator / clock generator (14 ultralow-jitter outputs) for ADRV9009 RF and JESD204B clocking
- 24x GTH transceiver lanes up to 12.5 Gbps (JESD204B for ADRV9009 synchronisation, 100GbE, PCIe Gen3) brought to P1 mezzanine connector
- PS-GTR transceivers up to 6 Gbps providing USB3.0, SGMII Ethernet, DisplayPort to P2 connector
- Marvell 88E1512 10/100/1000 Mbps Ethernet PHY (RGMII to ZU11EG PS GEM3) — RJ45 + magnetics on carrier
- Microchip USB3320C USB 2.0 ULPI PHY (ZU11EG PS USB0)
- ADM1177 hot-swap controller with integrated 12-bit I2C current/voltage monitor
- ADM1266 voltage sequencer/supervisor with non-volatile blackbox event recording
- 2x SAMTEC SEARAY 400-pin mezzanine connectors (P1: RF/GTH/clocks, P2: PS MIO/GTR/Ethernet/USB/SD/JTAG)
- 12V 120W single-supply input via mezzanine connectors
- Heat spreader plate fitted at manufacturing (AMD SP3/TR4/sTRX4 socket pattern for active cooler)
- Over-temperature protection: PWR_FAULT1 asserted at 65°C, power shutdown at 90°C

## Notes

### Device part number

The published Analog Devices documentation names the FPGA only as "Zynq UltraScale+ ZU11EG"; speed grade, package and temperature grade are not stated on the freely-available wiki pages or product page. The part `XCZU11EG-1FFVC1760I` is a **best-guess** based on:

- The user guide's "GTH transceivers run up to 12.5 Gb/s" rate matches the -1 speed grade.
- The hardware overview lists **24× GTH transceiver lanes**, which excludes the FFVC1156 package (16 GTH) and requires FFVC1760, FFVE1517 or FFVF1517.
- Industrial temperature grade (-I) matches the active-cooling / 90°C over-temp protection design.

The exact package and speed grade should be **confirmed against the Rev G schematic or BOM** (linked from the [ADRV9009-ZU11EG wiki](https://wiki.analog.com/resources/eval/user-guides/adrv9009-zu11eg/hardware)) before merge.

### Operating notes

- Requires **active cooling**; will thermally shut down within minutes under normal load without a fan. The kit ships with a heatsink + fan designed to mount on the SoM's heat spreader plate via the AMD SP3-style threaded pattern.
- Mates with the **ADRV2CRR-FMC** carrier (not the ADRV1CRR-FMC, which is for the ADRV9361-Z7035 / ADRV9364-Z7020 family).
- Multi-SOM synchronisation supported via the on-board HMC7044B clock tree and a SYNC pulse; up to 3 carriers can be chained from a single synchronisation board.
