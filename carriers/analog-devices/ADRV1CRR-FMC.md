---
mpn: ADRV1CRR-FMC
name: ADRV1CRR-FMC
status: active
url: https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv1crr-fmc.html
vendor: analog-devices
price: null
---

## PCIe
- Edge Gen2 x1

## Networking
- 1GbE x2
- SFP+ x1

## Video
- HDMI Out x1

## Expansion
- FMC LPC "FMC"
- Pmod x3

## Storage
- microSD x1

## USB
- Type-A 2.0 host x2

## USB UART/JTAG
- Micro-B UART

## User I/O
- LEDs x4
- Pushbuttons x4

## Extras
- General-purpose SMA breakout for 1x serial transceiver lane (Zynq GTX, up to 6.6 Gbps) from the mated SoM
- 2x audio TRS jacks (line / headphone)
- Camera ribbon-cable (FPC) connector
- BNC connector (J1) for external AD9361 reference clock input (selectable vs on-SoM 40 MHz XO via Zynq PL pin / device-tree gpio0 105)
- Power input via barrel jack with on/off slide switch
- DONE / RESET status LEDs + reset push-button
- Configuration-mode slide switches
- One RJ45 Ethernet is wired RJ45-only (PHY on the SoM via Zynq PS GEM); the second RJ45 uses an on-carrier PHY routed through SoM PL pins and is only fully usable with the ADRV9361-Z7035 (the ADRV9364-Z7020 SoM lacks the spare PL I/O for it)

## Notes

The ADRV1CRR-FMC is the **FMC carrier** for Analog Devices' SDR System-on-Module family. Compatible SoMs: **ADRV9361-Z7035** (full functionality) and **ADRV9364-Z7020** (subset — HDMI Out, Camera, PMOD0, SFP+, LEDs 1-3, slide switches, push-button 0 and the FMC connector are not supported on the Z7020 due to its smaller pin count). The ADRV9009-ZU11EG uses a different carrier (ADRV2CRR-FMC).

The four GTX serial transceivers from the mated SoM are allocated as:

| Lane | Destination |
|---|---|
| 1 | PCIe Gen2 x1 card-edge connector |
| 2 | FMC LPC connector |
| 3 | SFP+ cage |
| 4 | General-purpose SMA break-out |

The carrier has no FPGA of its own; all programmable logic is provided by the mated SoM. The Pmod tally (3) covers PMOD0, PMOD1 and PMOD_MIO from the wiki user guide — PMOD_MIO is wired to Zynq PS MIO pins rather than the PL.
