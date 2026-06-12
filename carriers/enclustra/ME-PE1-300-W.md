---
mpn: ME-PE1-300-W
name: Mercury+ PE1-300
status: active
url: https://www.enclustra.com/en/products/base-boards/mercury-pe1-300-400/
vendor: enclustra
price: { value: 642, currency: USD }
---

## PCIe
- Edge Gen2 x4
- MiniPCIe-Full +mSATA

## Clocking
- Programmable
- SMA clock in x1
- SMA clock out x1

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
- FMC HPC "FMC1" VADJ 1.8-3.3V
- Pmod x3

## Extras
- 2x 40-pin Anios I/O extension pin headers
- System controller with power control and current sense
- System monitor
- mPCIe/mSATA card holder (USB signals only)
- SIM card holder (optional)
- MGT lanes routed to SMA connectors (optional)
- 5 to 12V DC single supply (USB bus power with restrictions)
- Hirose FX10 connectors for Mercury / Mercury+ modules
- Temperature range -25..+85 C
- Micro USB 2.0 device interface also exposes SPI and I2C

## Notes

The available features depend on the equipped Mercury FPGA/SoC module and the selected PE1 board model. The -300 variant fits a low-jitter clock generator, system monitor, power control and current sense. The SMA clock / MGT and SIM-card options are populated to order.

FMC VADJ (VCC_ADJ) follows the module I/O voltage VCC_IO_B, selected by the I/O voltage selection jumpers on J2000: 3.3 V (VCC_3V3) or the module-dependent VCC_OUT_A / VCC_OUT_B supply outputs (typically 1.8-2.5 V; supported envelope 1.8-3.3 V depending on the mounted Mercury module). The factory default jumper positions (2-4, 8-10) apply no I/O voltage at all, so the VADJ rail is unpowered until the jumpers are set; the board does not read the FMC IPMI EEPROM.
