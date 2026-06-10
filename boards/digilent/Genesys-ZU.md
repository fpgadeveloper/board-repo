---
mpn: Genesys-ZU
name: Genesys-ZU
status: active
url: https://digilent.com/shop/genesys-zu-zynq-ultrascale-mpsoc-development-board/
vendor: digilent
price: { value: 1995, currency: USD }
device: { part: XCZU5EV-1SFVC784E, vendor: amd-xilinx }
---

## Memory
- DDR4 4GB SODIMM

## Flash
- QSPI 32MB

## PCIe
- MiniPCIe-Half x1
- MiniPCIe-Full x1 +mSATA

## Audio
- Codec ADAU1761
- Headphone x1
- Microphone x1

## Video
- HDMI In x1
- HDMI Out x1
- DisplayPort x1
- MIPI CSI x2

## Networking
- 1GbE x1
- SFP+ x1

## USB
- Type-C 3.1 OTG
- Type-A 2.0 host x2

## USB UART/JTAG
- Micro-B JTAG/UART

## Expansion
- FMC LPC "LPC" VADJ 1.2-1.8V
- Pmod x4
- SYZYGY x1

## Storage
- microSD x1

## User I/O
- LEDs x5
- Pushbuttons x7
- DIP switches x4

## Wireless
- WiFi

## Features
- Programmable VADJ

## Notes

VADJ supports 1.2 V / 1.5 V / 1.8 V (discrete values, ±5%). On current boards
(Rev. D, Platform MCU firmware 2.0) the Platform MCU (ATmega328PB) reads the FMC
mezzanine's IPMI EEPROM at power-up and sets VADJ to the highest commonly
supported value — the rail stays disabled (PMCU LED fault) if there is no common
value. The PL can override the negotiated voltage via the VADJ_LEVEL1/VADJ_LEVEL0
+ VADJ_AUTON pins; on Rev. B boards (firmware 1.0) there is no auto-negotiation
and the PL must request a level this way. The VADJ rail is shared by the FMC
slot, the SYZYGY/Zmod port, and Pmod JA, so all attached modules must accept the
same voltage.
