---
mpn: MK-A5E065BB32AEA
name: Agilex 5 E-Series 065B Modular
status: active
url: https://www.altera.com/products/devkit/po-3274/agilex-5-fpga-and-soc-e-series-065b-modular-development-kit
vendor: altera
price: { value: 1995, currency: USD }
device: { part: A5ED065BB32AE4S, vendor: altera }
---

## Memory
- DDR4 8GB 32-bit
- DDR4 8GB 40-bit ECC
- DDR4 8GB 40-bit ECC

## Flash
- QSPI 256MB

## Networking
- 2.5GbE x2
- SFP28 x1

## PCIe
- Edge Gen4 x4

## Video
- HDMI In x1
- HDMI Out x1
- DisplayPort x2
- SDI In x1
- SDI Out x1
- MIPI CSI x2

## Expansion
- FMC+ "J7" VADJ 1.2V
- GPIO Header x2

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
- SMA clock in x2
- SMA clock out x2

## Features
- Power monitoring

## Extras
- USB Type-C connector (USB 3.1 on transceiver bank 1C, UX2)
- Tri-level sync connector (J19)
- Two-board kit: 113 x 94 mm modular board on a 254 x 111 mm PCIe form-factor carrier board
- Built-in USB Blaster III FPGA Development Cable; separate 2x5 JTAG header
- MAX 10 (10M16DAF256I6G) system controller for power sequencing and JTAG chain topology

## Notes
### Transceiver bank map

| Bank | Use |
|---|---|
| UX 1A | FMC+ XCVR lanes 4-7 (17 Gbps max) and GBTCLK1_M2C |
| UX 1B | FMC+ XCVR lanes 0-3 (17 Gbps max) and GBTCLK0_M2C |
| UX 1C | UX0/UX1 2.5G TSN Ethernet, UX2 USB 3.1, UX3 SFP28 (10G) |
| UX 4A | DisplayPort 2.0 |
| UX 4B | HDMI 2.0 |
| UX 4C | PCIe Gen4 x4 (x16 edge connector) |

Each FMC quad carries its own mezzanine reference clock: bank 1B takes
GBTCLK0_M2C from J7.D4/D5, bank 1A takes GBTCLK1_M2C from J7.B20/B21.

CvP (Configuration via Protocol) is not supported. CvP needs a PCIe link on
banks 1A/1B/1C, and none of those are wired to the PCIe edge connector. The
FMC+ interface on banks 1A/1B is not compatible with the FMC+ to PCIe edge
connector cable.

### FMC connector reference numbers

The connector table in the user guide (820977) is offset by one row: the
functionality column lags the connector column. The FMC+ connector is **J7**,
not J14 - confirmed by the carrier schematic (150-330724-B1), which routes
`FMC_GBTCLK0_M2C_DP` to J7.D4 and `FMC_GBTCLK1_M2C_DP` to J7.B20.

### FMC power

| Rail | Regulator / protection | Limit |
|---|---|---|
| +V12P0_FMC | MP5016GQH-L eFuse | ISET = 1.5 A |
| +V3P3 (shared with HDMI, DP, 2.5G PHY, oscillators, Si53254) | -- | 7.5 A rail |
| +V1P2_FMC_ADJ (VADJ) | MPM3632C | 2 A |

VADJ is 1.2 V as built. The carrier carries a strap (R591) documented as
`FMC_VADJ=1.8V`, and R774 (the 1 mOhm sense resistor in the VADJ path) is
marked "to be unmounted to support AD9176 FMC add-in card".

### FMC reference clock alternatives

Both FMC transceiver banks have a second reference clock input fed from
on-board programmable oscillators, so a mezzanine-supplied clock is optional:

- Bank 1B "G" refclk (AY115/AY120) <- `CLK_MUX_SI5518_OUT4_SI569_SI549`,
  selectable between Si5518 OUT4, Si549 (U34) and Si569 (U33), 100 MHz default
- Bank 1A "G" refclk (BC107/BC111) <- Si5518 OUT6, mux-selectable to
  156.25 / 148.35 / 148.5 / 100 MHz

Bank 1B's GBTCLK0 input additionally passes through a mux (clk_mux_6_sel,
EU21) that can substitute the on-board Si549 for the mezzanine clock. All FMC
GBTCLK inputs are AC-coupled on the carrier (0.1 uF).

### Board revisions

Available as Rev C2 and Rev C3, which differ in board population and power
path selection.
