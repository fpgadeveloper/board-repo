---
mpn: DK-A5E065BB32AEA
name: Agilex 5 E-Series 065B Premium
status: active
url: https://www.altera.com/products/devkit/po-3284/agilex-5-fpga-e-series-065b-premium-development-kit
vendor: altera
price: { value: 3125, currency: USD }
device: { part: A5ED065BB32AE4S, vendor: altera }
---

## Memory
- DDR4 8GB 40-bit ECC
- DDR4 8GB 40-bit ECC
- LPDDR4 4GB 32-bit

## Flash
- QSPI 256MB

## Networking
- 1GbE x2
- 2.5GbE x1
- QSFP+ x2
- SFP+ x2

## Video
- MIPI CSI x1

## High-speed I/O
- SMA x2 GTS 17.16Gbps

## Expansion
- FMC+ "J34" VADJ 1.2-1.3V

## Storage
- microSD x1

## USB UART/JTAG
- Micro-B JTAG

## User I/O
- LEDs x4
- Pushbuttons x4
- DIP switches x4

## Clocking
- Programmable

## Features
- Power monitoring

## Extras
- HPS Expansion Board on the ADM connector, carrying USB 3.1 Gen 1, an RS-232 UART, a 1GbE RJ45 and the micro SD card slot
- Board powered from a PCIe slot plus the required 2x4 auxiliary power connector
- Built-in Intel FPGA Download Cable II; separate JTAG header
- MAX 10 (10M50DAF484) system controller for power sequencing, JTAG chain topology and fan control

## Notes
### Transceiver bank map

All 24 GTS channels (6 banks x 4) are committed:

| Bank | Use |
|---|---|
| UX 1A | QSFP+ #1 (J12), 4 lanes |
| UX 1B | QSFP+ #2 (J13), 4 lanes |
| UX 1C | SGMII 2.5G RJ45 (J41) + USB 3.1 on the HPS card |
| UX 4A | SFP+ #1 (J14), SFP+ #2 (J15), 2x SMA (17G) |
| UX 4B | FMC+ DP4-DP7 and GBTCLK1_M2C |
| UX 4C | FMC+ DP0-DP3 and GBTCLK0_M2C |

The FMC+ site therefore presents two whole quads, each with its own
mezzanine-supplied reference clock in the same bank as its lanes.

**Documentation error:** Table 21 (FMC Connector J34) in the user guide
(814550) lists the I/O Bank column with 4B and 4C swapped relative to both the
prose in section A.8.4 and the production schematic (150-0330713-A3). The
schematic is authoritative: `FMC_RX0_P` -> `GTSR4C_RX_CH0P` and
`FMC_GBTCLK0_M2C_P` -> `REFCLK_GTSR4C_CH1P` (both bank 4C); `FMC_RX4_P` and
`FMC_GBTCLK1_M2C_P` are both in bank 4B.

### FMC power

| Rail | Protection | Limit |
|---|---|---|
| 12V_FMC | MAX17613AATP+T, latch-off | 1.29 A |
| 3V3_FMC | TPS25957 load switch | -- |
| 1V2_FMC (VADJ) | TPS22975 load switch | -- |

VADJ is adjustable between 1.2 V and 1.3 V only. The user guide states the kit
"does not support FMC cards that are not compliant with Agilex 5 FPGA
1.2-V/1.3-V I/O standard".

### FMC reference clocks

Each FMC transceiver bank also has a second reference clock input driven from
an on-board programmable oscillator, so a mezzanine clock is not mandatory:

- Bank 4B `REFCLK_GTSR4B_RX` <- `FMC_VCXO_REFCLK` (Si569 VCXO X5, 148.35 MHz
  default, switchable to 148.5 MHz, LVDS 2.5 V)
- Bank 4C `REFCLK_GTSR4C_RX` <- `FMC_PROG_REFCLK` (Si548 XO X6, 135 MHz
  default, LVDS 2.5 V)

The GBTCLK0/1_M2C inputs are AC-coupled on the carrier (0.22 uF).
