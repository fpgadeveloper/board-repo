---
mpn: STEMlab-125-14-PRO-Z7020-Gen-2
name: STEMlab 125-14 PRO Z7020 Gen 2
status: active
url: https://redpitaya.com/product/stemlab-125-14-pro-z7020-gen-2-oem/
vendor: redpitaya
price: { value: 889, currency: EUR }
device: { part: XC7Z020-1CLG400C, vendor: amd-xilinx }
---

## Memory
- DDR3 1GB 32-bit

## Analog
- ADC LTC2145-14 2ch 14-bit 125MSPS
- DAC AD9767 2ch 14-bit 125MSPS

## Networking
- 1GbE x1

## USB
- Type-C 2.0 host

## USB UART/JTAG
- Type-C UART

## Storage
- microSD x1

## User I/O
- LEDs x8

## Extras
- Two RF inputs on SMA connectors (±1V/±20V full scale selected by LV/HV jumpers, DC coupled, 1MΩ, DC-60MHz) and two RF outputs on SMA connectors (±1V into 50Ω, ±2V into Hi-Z)
- Extension connectors E1/E2 (2x13 IDC 2.54mm): 22 digital I/O (3.3V, usable as 11 differential pairs) with 2x software-selectable CAN, 4 slow analog inputs (12-bit, 0-7.0V), 4 slow PWM analog outputs (8-bit, 0-1.8V), SPI/UART/I2C, ±5V and +3.3V supply pins
- E3 high-speed extension connector (2x20 0.5mm Micro Blade & Beam): 8 LVDS differential pairs (2.5V, bank 13), QSPI/eMMC external boot interface, I2C, power and watchdog control, for use with the optional QSPI eMMC (E3) add-on module
- External ADC/DAC/FPGA sampling clock input (1-125MHz, AC coupled) on E2 with internal/external selection via the CLK_SEL pin and an NB6L72 crosspoint switch
- External trigger input and trigger output on E1 (DIO0_P / DIO0_N)
- Two USB-C daisy-chain connectors (S1 transmit, S2 receive) carrying 1.8V FPGA clock/trigger links up to 500Mb/s for multi-board synchronisation
- JTAG connector (6-pin header)
- USB-C 5V/3A power input (alternatively +5V via E2)

## Notes

- **S1/S2 are not USB ports:** the USB-C daisy-chain connectors are DC-coupled FPGA links that do not follow the USB-C specification. Only connect them to another Red Pitaya S1/S2 connector; use the HOST USB-C port for peripherals.
- **E3 bank voltage:** the E3 fast differential pairs (DIO11-DIO18) sit on Zynq bank 13, powered at 2.5V by default, and are not 3.3V tolerant. Bank 13 can be moved to 3.3V by relocating ferrite bead FB26 to FB25, which also changes the level of DIO8-DIO10 on E1.
- **Boot source:** SDIO_SEL (E3 pin 6) selects the boot device before power-on — low (default) boots from the microSD card, high boots from QSPI/eMMC on an E3 add-on module. With the QSPI eMMC module fitted the board does not power up automatically; press P-ON on the module.
- **External clock:** E2 pin 21 (CLK_SEL) high or unconnected selects the on-board 125MHz oscillator; tie it to GND to use Ext. ADC Clk± (E2 pins 23/24). This input drives the ADC/DAC/FPGA sampling clock directly — it is not a PLL reference, and changing its frequency at runtime requires an FPGA reset. Without a valid external clock the FPGA does not run (OS older than 2.07-48 fails to boot).
- **Power supply:** use a 5V/3A USB-C supply with functional CC lines. A 2-wire 5V supply works via the E2 +5V pin, or through USB-C with jumper JP5 bridged; in both cases the Power Error LED lighting is expected.
- **Slow analog input range:** the E2 auxiliary analog inputs have an actual full-scale range of 0-7.0V, not the 0-3.5V quoted in older specifications.
