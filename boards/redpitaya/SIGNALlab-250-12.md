---
mpn: SIGNALlab-250-12
name: SIGNALlab 250-12
status: active
url: https://redpitaya.com/signallab-250-12/
vendor: redpitaya
price: { value: 1751, currency: EUR }
device: { part: XC7Z020-3CLG400E, vendor: amd-xilinx }
---

## Memory
- DDR3 1GB 32-bit

## Analog
- ADC AD9613 2ch 12-bit 250MSPS
- DAC AD9746 2ch 14-bit 250MSPS

## Clocking
- Programmable
- SMA clock in x1

## Networking
- 1GbE x1

## USB
- Type-A 2.0 host x2
- Header 2.0 host

## USB UART/JTAG
- Type-C UART

## Storage
- microSD x1

## User I/O
- LEDs x10

## Extras
- Two RF inputs and two RF outputs on BNC connectors with software-selectable ranges (inputs ±1V/±20V with AC/DC coupling, outputs ±2V/±10V into Hi-Z)
- External trigger input on BNC connector
- 10MHz reference clock input on SMA (back panel) for PLL locking of the Si571 VCXO
- External LVDS ADC/DAC/FPGA sampling clock input on the E2 extension connector
- Extension connectors E1/E2 (2x13 IDC 2.54mm): 19 digital I/O (3.3V), 2x CAN, 4 slow analog inputs (12-bit), 4 slow PWM analog outputs, I2C/SPI/UART, USB 2.0
- Two eSATA daisy-chain connectors (S1/S2) wired to FPGA I/O, up to 500Mb/s
- Power over Ethernet (PoE) or 12-26V DC barrel-jack input
- Aluminium enclosure (Standard kit); OEM version ships as a bare board with heatsink

## Notes

- **UART TX on E2 at power-up:** PS_MIO8 (UART TX, E2 pin 7) is output-only and must be grounded or left floating at power-up — an external device driving it high during boot can stop the board from booting. Buffer it (e.g. open-drain buffer with pull-up) when designing extension hardware.
- **S1/S2 daisy-chain connectors:** these eSATA-style connectors carry 1.8V FPGA I/O and are not compatible with SATA storage devices. Unlike the STEMlab 125-14, the shared clock does not reach the ADC/DAC, so multi-board synchronisation uses the 10MHz SMA reference input plus the BNC trigger instead.
- **Slow analog input range:** the E2 auxiliary analog inputs (AI0-AI3) have an actual full-scale range of 0-7.0V, not the 0-3.5V quoted in older specifications.
- **Enclosure:** the aluminium housing must be removed to reach the E1/E2 extension connectors.
