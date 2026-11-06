---
title: "Microclimate OS - Smart Lawn Care System"
author: "Wankabakov"
description: "Building an ESP32 microclimate telemetry node with LoRaWAN for smart lawn care."
created_at: "2026-10-01"
---

# October 01: Initial idea & basic analog sensors

Started working on the smart lawn care project. The goal is to monitor ground moisture and temperature to know when the grass actually needs water. Hooked up some super cheap analog soil moisture sensors and a basic DHT11 to an Arduino Uno. Readings were jumping all over the place. Turns out cheap soil probes corrode in like two days, lol. Spent hours trying to calibrate raw ADC values.

**Total time spent: 6 hours**

# October 04: Setting up a local Raspberry Pi server

Decided to send data to a local server instead of just printing to serial. Set up a Raspberry Pi with a basic Python Flask server and a SQLite database. Spent half the day wrestling with Linux permissions, static IPs, and router port forwarding just so the local board could talk to the Pi. Got local data logging working, but range was limited to WiFi coverage.

**Total time spent: 8 hours**

# October 08: Testing Infrared (IR) thermal sensors

Realized soil temperature isn't enough; surface heat matters for turf health. Tried adding an infrared thermal sensor (MLX90614) to measure the actual grass leaf temperature without touching it. Had massive I2C address conflicts with the existing setup and spent hours debugging why the sensor kept hanging the I2C bus. Fixed it with proper pull-up resistors.

![Circuit Setup](circuit.jpg)

**Total time spent: 7 hours**

# October 12: Switch to ESP32 & battery power constraints

The Arduino + Pi setup was way too power-hungry to run on a battery in the middle of the lawn. Switched the main controller to an ESP32 for deep sleep capabilities. Rewrote the entire sensor acquisition codebase in MicroPython. Spent a full day fighting deep sleep wake-up timers and managing power spikes when sensors turn on.

**Total time spent: 9 hours**

# October 15: Upgrading to LoRaWAN (LA66 Module)

WiFi in the garden was unreliable, so I jumped to LoRaWAN. Got the LA66 module and spent hours reading datasheets to figure out AT commands and UART communication. Connected ESP32 GPIO 17 (TX) to LA66 RX (Pin 11) and GPIO 16 (RX) to LA66 TX (Pin 10). Spent forever troubleshooting missing payloads before realizing I swapped RX and TX, lol classic mistake.

**Total time spent: 7 hours**

# October 18: CAD design & 3D printing weatherproof enclosure

Designed a 3D printable case to house the ESP32, LA66 module, BME280, IR sensor, and battery. Had two failed prints because the print bed wasn't leveled properly (pain). Third print succeeded. Stuffing all the wiring, battery pack, and antenna into the tight enclosure without snapping wires was basically high-stakes Tetris.

![3D Printed Case](case.jpg)

**Total time spent: 6 hours**

# October 21: Dashboard integration with loramint.de

Integrated the node with the `loramint.de` platform for live telemetry visualization. Wrote payload formatters to unpack raw LoRaWAN bytes into actual temperature, humidity, and pressure values. Debugged connection stability and finalized the codebase in the `/code` folder. Seeing live grass-level data plot smoothly on the web dashboard was incredibly satisfying!

**Total time spent: 5 hours**---
title: "My Project Name"
author: "your-name"
description: "A short description of your project"
created_at: "2026-03-20"
---

# March 20: Designed the PCB layout

Spent the day laying out traces in KiCad. Got the power section done
and started routing the signal lines. Ran into some clearance issues
with the USB connector footprint but found a workaround.

![pcb layout](images/pcb-v1.png)

**Total time spent: 4 hours**

# March 21: Ordered components

Placed orders for all the SMD parts from LCSC. Also found a better
LDO regulator that saves board space.

**Total time spent: 1 hour**

# March 23: PCB arrived, started soldering

The boards came in! Soldered the first prototype. Two pads were
bridged on the QFN package — had to wick and redo them.

![soldering](images/soldering.jpg)

**Total time spent: 3 hours**
