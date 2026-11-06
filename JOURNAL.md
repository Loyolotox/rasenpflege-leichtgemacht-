---
title: "Rasenpflege Leichtgemacht - Microclimate OS"
author: "Wankabakov"
description: "Building an automated lawn monitoring system using sensors, Raspberry Pi, ESP32, and LoRaWAN telemetry."
created_at: "2026-10-01"
---

# October 01: Starting the lawn care project with basic sensors

So, the whole idea started because maintaining a proper lawn is actually painful without data. Today I decided to build a monitoring system. Hooked up some super cheap analog soil moisture sensors and a basic temperature sensor to an Arduino. Plugged everything into the breadboard and started reading raw ADC values. Total disaster — the cheap metal probes started oxidizing almost immediately in the damp dirt, lol. But hey, it’s a start for the lawn care tracker!

**Total time spent: 6 hours**

# October 04: Setting up the Raspberry Pi local server

Realized that just reading sensor values on an Arduino isn't enough; we need a proper backend to store historical data about the lawn conditions. Set up an old Raspberry Pi with a Python Flask server and a local SQLite database. Spent half the day fighting with Linux network configurations, static IPs, and router settings so the microcontroller could actually talk to the Pi over local Wi-Fi without dropping packets every five minutes. 

**Total time spent: 8 hours**

# October 08: Adding an Infrared (IR) sensor for surface turf temperature

Soil temperature alone doesn't tell the whole story about grass health, so today we integrated an MLX90614 infrared thermal sensor to measure the surface temperature of the lawn without physical contact. Naturally, I ran straight into I2C address conflicts with the existing hardware setup. Spent hours staring at the serial monitor while the code froze completely. Added proper pull-up resistors and tweaked the code until the IR sensor finally behaved.

![Circuit Setup](circuit.jpg)

**Total time spent: 7 hours**

# October 12: Moving away from Arduino & Pi to the ESP32

Big realization today: an Arduino combined with a running Raspberry Pi server eats way too much power to be a practical, standalone garden node out in the yard. Switched the main brain over to an ESP32 because of its deep sleep features. Had to rewrite a massive chunk of the sensor acquisition code into MicroPython. Spent hours debugging deep sleep wake-up timers because the board refused to wake up properly when triggered by the sensor interrupts. Classic embedded dev pain, lol.

**Total time spent: 9 hours**

# October 15: Upgrading to LoRaWAN with the LA66 module

Wi-Fi coverage in the middle of the garden is absolute garbage, so local Wi-Fi was out of the question. Decided to jump straight to LoRaWAN using an LA66 module. Wired up ESP32 GPIO 17 (TX) to LA66 RX (Pin 11) and GPIO 16 (RX) to LA66 TX (Pin 10), plus 3V3 and GND power lines. Spent ages digging through obscure datasheets trying to figure out the right AT commands. Accidentally swapped RX and TX on the first try, meaning nothing transmitted at all for two hours until I noticed the mistake. Lol, rookie error.

**Total time spent: 7 hours**

# October 18: CAD design & 3D printing a weatherproof lawn case

Leaving exposed electronics out in the grass is a great way to destroy a project instantly. Spent the day designing a custom weatherproof enclosure in CAD to safely house the ESP32, the LA66 module, the BME280 sensor, the IR sensor, and the battery pack. The first 3D print failed midway because the bed adhesion let go (pain). Second print worked, but stuffing all the wiring, antennas, and batteries inside without snapping any jumper wires felt like playing high-stakes, stressful Tetris.

![3D Printed Case](case.jpg)

**Total time spent: 6 hours**

# October 21: Pushing telemetry data to loramint.de dashboard

Final stretch for the lawn care system! Connected the node to the `loramint.de` platform to visualize all the microclimate telemetry live. Wrote custom payload formatting scripts to translate raw LoRaWAN byte arrays into actual human-readable temperature, humidity, and soil metrics. Debugged some packet loss issues out in the yard. Seeing the actual live grass data plotting smoothly on the web dashboard made all the debugging hours totally worth it!

**Total time spent: 5 hours**
