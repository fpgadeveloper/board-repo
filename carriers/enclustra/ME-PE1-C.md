---
mpn: ME-PE1-C
name: Mercury+ PE1
status: active
url: https://www.enclustra.com/en/products/base-boards/mercury-pe1-300-400/
vendor: enclustra
price: null
---

## PCIe
- Edge Gen2 x4

## Networking
- 1GbE x2 RJ45-only

## USB
- Type-A 2.0 host x4
- Micro-B 3.0 device

## USB UART/JTAG
- Micro-B JTAG/UART

## Storage
- microSD x1

## Expansion
- Pmod x3

## Extras
- 2x 40-pin Anios I/O extension pin headers
- System controller
- 5 to 12V DC single supply (USB bus power with restrictions)
- Hirose FX10 connectors for Mercury / Mercury+ modules
- Micro USB 2.0 device interface also exposes SPI and I2C
- FMC connector(s) — count and type (LPC/HPC) depend on the configured board model (200/300/400)

## Notes

ME-PE1-C is the generic Mercury+ PE1 base-board article; the populated options — FMC LPC vs HPC count, clock generator, system monitor, mPCIe/mSATA holder, SMA/MGT and SIM-card options — depend on the selected board model (PE1-200 / PE1-300 / PE1-400). See the model-specific articles (ME-PE1-200-C, ME-PE1-300-W, ME-PE1-400-W) for the per-model feature set.

The available features also depend on the equipped Mercury FPGA/SoC module.

The FMC connector I/O pins connect directly to the FPGA/SoC on the Mercury module and run at the module I/O voltage: VCC_IO_A / VCC_IO_B are selected with jumper J1800 among 3.3 V (VCC_3V3) or the module-dependent VCC_OUT_A / VCC_OUT_B supply outputs. The factory default jumper positions (1-3, 9-11) apply no I/O voltage at all, so the I/O rails are unpowered until the jumpers are set; the board does not read the FMC IPMI EEPROM. See the model-specific articles for per-slot VADJ ranges.
