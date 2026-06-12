---
mpn: Atum-A5
name: Atum A5
status: active
url: https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=2&No=1343
vendor: terasic
price: { value: 1999, currency: USD }
device: { part: A5ED065BB32AE4SR0, vendor: altera }
---

## Memory
- DDR4 4GB 32-bit
- DDR4 4GB 32-bit

## Flash
- QSPI 64MB
- eMMC 8GB

## Sensors
- Temperature

## PCIe
- iPass Gen3 x4

## Video
- HDMI Out x1
- MIPI CSI x2

## Networking
- 1GbE x1
- 2.5GbE x1
- QSFP+ x1

## USB UART/JTAG
- Type-C JTAG

## Expansion
- FMC+ "FMC+" VADJ 1.2V
- GPIO Header x2

## Storage
- microSD x1

## User I/O
- LEDs x5
- Pushbuttons x5
- DIP switches x4

## Features
- Power monitoring

## Extras
- USB 3.1 Gen1 Type-C port (HPS)
- 2x6 TMD header

## Notes

The FMC+ VADJ supply is fixed at 1.2 V (4 A max). Separately, jumper JP1 ("FMC+ HAB VCCIO Select Header") sets the VCCIO of the FPGA bank driving the HA/HB signal pins to 1.2 V (default) or 1.3 V — this changes the I/O standard of those signals only, not the documented VADJ power pin voltage. The board does not read the FMC IPMI EEPROM.
