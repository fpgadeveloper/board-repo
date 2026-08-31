---
mpn: Forgix
name: Forgix
status: active
url: https://forgix.tech/
vendor: adiuvo
price: { value: 50, currency: USD }
device: { part: T8F49I2, vendor: efinix }
---

## Memory
- PSRAM 2MB

## Flash
- QSPI 2MB

## USB
- Type-C 1.1 device

## User I/O
- RGB LEDs x1
- Pushbuttons x1

## Extras
- Raspberry Pi RP2354A MCU (dual Cortex-M33 / RISC-V, 2MB in-package QSPI flash) paired with the Trion T8 FPGA
- Teensy 4.0-compatible 28-pin footprint, breadboard-friendly
- Through-hole and castellated edge pads routed to either the RP2354A or the FPGA
- RP2354A interfaces broken out to the edge pads: SPI, I2C, UART, ADC, USB 1.1
- FPGA configured in SPI passive mode by the RP2354A — no separate FPGA programmer required
- External FPGA oscillator (ECS-2520MV), enable-gated by the RP2354A via OSC_EN
- SWD debug on a Tag-Connect TC2030-NL footprint
- 3.3V FPGA I/O rail, 1.1V FPGA core rail
- USB-C powered, with ideal-diode power path and separate VIN / VBAT supply inputs

## Notes

The FPGA is fitted as **T8F49I2X**. Efinix's own Trion Selector Guide documents the
orderable code for this device as `T8F49I2` (T8 die, 49-ball FBGA, industrial temperature,
speed grade 2); the trailing `X` is a distributor packaging suffix and is not part of the
Efinix ordering-code grammar, so the catalog records the base code.

There is no JTAG header and no FPGA configuration flash. The RP2354A holds the FPGA
bitstream and streams it to the Trion over SPI in passive mode (x1) on every power-up.
Adiuvo publishes an open-source "Forge FPGA Loader" — RP2354A firmware plus a Python
host GUI/CLI that sends an Efinity SPI-passive `.hex`/`.bin` image over USB CDC serial.
