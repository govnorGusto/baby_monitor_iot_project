# Simple "Real-Time" Baby monitor
Author: Gustav Hardselius<br>
ID: gh222mp

## Overview
This project is how you go about to make a simple "real-time" baby monitor. It measures 2 different temperatures, humidity and has sound detection (for the screams). It dsplays current values as well as monitoring if the sound i high over time. This is a beginners to intermediate project and the estimated time needed to complete this project following this tutorial is 3-4 hours.

## Objective
The purpose of this project is to be able to monitor your baby when its sleeping in a stroller. This will be done by using two different temperature sensor (outside temp and the temp close to the baby), humidity and sound detection in real-time, (this also monitors if a high sound is detected over time, so we could rule out a sudden sound).

A microcontroller and 3 different sensors is used to collect data. This data is transmitted through an MQTT server and displayed on the internet.

## Material

In this project we will work with the Raspberry Pi Pico WH microcontroller. It offers both digital and analog input and output. It's super tiny, and it is has a WiFi intecface. For detailed information about the Pico W, check out the [datasheet](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf).

To measure temperatures and humidity we will use DHT11 Humidity and Temperature Sensor, The MCP9700 analog thermistor and KY-038 Sound detector sensor.

We also need a breadboard and some jumpers to connect everything, and a micro-USB cable to connect to our computer, this will also second as a power source.

Table of components bought at electroki

|                                                                                                                               | Material             | Price (SEK) |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| <img src='https://www.electrokit.com/uploads/productimage/41019/PICO-WH-HERO.jpg' width=150>  | Raspberry Pi Pico WH | 109         |
| <img src='https://www.electrokit.com/uploads/productimage/41015/41015728-1.jpg' width=150>    | DHT11                | 49          |
| <img src='https://www.electrokit.com/uploads/productimage/41016/41016355.jpg' width=150>      | MCP9700              | 39          |
| <img src='https://www.electrokit.com/uploads/productimage/41015/41015706.jpg' width=150>      | KY-038               | 36          |
| <img src='https://www.electrokit.com/uploads/productimage/10160/10160840.jpg' width=150>      | Breadboard           | 69          |
| <img src='https://www.electrokit.com/uploads/productimage/41012/41012909.jpg' width=150>      | Jumper cables M-to-M | 29          |
| <img src='https://www.electrokit.com/uploads/productimage/41002/41002871-1.jpg' width=150>    | USB-cable A male – mini B male 5p   | 39          |
