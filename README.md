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

Table of components bought at [electro:kit](https://www.electrokit.com).
|                                                                                                                               | Material             | Price (SEK) |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| <img src='https://www.electrokit.com/uploads/productimage/41019/PICO-WH-HERO.jpg' width=150>  | Raspberry Pi Pico WH | 109         |
| <img src='https://www.electrokit.com/uploads/productimage/41015/41015728-1.jpg' width=150>    | DHT11                | 49          |
| <img src='https://www.electrokit.com/uploads/productimage/41016/41016355.jpg' width=150>      | MCP9700              | 39          |
| <img src='https://www.electrokit.com/uploads/productimage/41015/41015706.jpg' width=150>      | KY-038               | 36          |
| <img src='https://www.electrokit.com/uploads/productimage/10160/10160840.jpg' width=150>      | Breadboard           | 69          |
| <img src='https://www.electrokit.com/uploads/productimage/41012/41012909.jpg' width=150>      | Jumper cables M-to-M | 29          |
| <img src='https://www.electrokit.com/uploads/productimage/41002/41002871-1.jpg' width=150>    | USB-cable A male – mini B male 5p   | 39          |

## Computer setup
This will work on a Windows, Mac or Linux machine, just be sure to download the right software for for your OS.

* For IDE we use [Visual Studio Code](https://code.visualstudio.com/)
  * with the extension [PyMakr](https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md) (which is used to upload code to the Pico WH.
  * To use the extension we also need to install [NodeJS](https://nodejs.org/en/download).

### Installation steps

1. Install [Python](https://www.python.org/downloads/) if you don't already have it installed.
2. Download and install [Node JS](https://nodejs.org/en/download). Get the current version, not the LTS.
3. Download and install the IDE [VS Code](https://code.visualstudio.com/).
4. Install [PyMakr](https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md) via the extension marketplace inside VS Code.
5. Update the firmware on your Raspberry Pi Pico:
   In order:
   * Download The [MicroPython firmware](https://micropython.org/download/rp2-pico-w/). This is a **uf2** file. Get the latest from **Releases**, not ~~Nightly builds~~.
   * Connect the micro-USB cable to the Raspberry Pi Pico.
   * While holding the **BOOTSEL** button down on the board, connect the other end of the USB cable to your computer. After plugging it in you can release the button.
   * A new drive should appear in your file system named **RPI-RP2**, this is the Raspberry Pi Pico storage. Just drag and drop the **uf2**, you downloaded earlier, into this storage. This will install micropython on your Raspberry Pi Pico.
   * Wait for the board to automatically disconnect and reconnect (should take less than a minute).
   * If you are using a Linux machine you need to do the following extra steps:
      * **Debian/Fedora**: enter this command into the terminal ``sudo usermod -a -G dialout $USER ``
      * **Arch**: enter the following command into the terminal
        ``sudo usermod -a -G uucp $USER``

## Putting everything together
This image illustrates how to connect the DHT11, MCP9700, and KY-038 to your Raspberry Pi Pico WH using a piece of bread.
<p align='center'>
<img src='https://github.com/gurkwaan/baby_monitor_iot_project/blob/main/img/breadboard.png?raw=true' width=800>
</p>

The KY-038 Sound sensor has both analog and digital outputs. In this project we will utilize the **Digital ONLY**, It will give us a HIGH value (1), when the sound detected is high enough. On this module is a potentiometer where you can adjust the sensitivity of the sound input. This is pretty tricky, the microphone is rather sensitive and will detect magnetic fields, blowing wind etc. 
<p align='center'>
<img src='https://github.com/gurkwaan/baby_monitor_iot_project/blob/main/img/400px-sens-poti-EN.png' width=800>
</p>

## Platform
For this project the choice of platform falls on **adafruit**. It is free and easy to use for beginners. It also offers some simple visuals for presenting your data.

 * First we need to set up an account at [adafruit IO](https://io.adafruit.com)
 * Next we create 4 feeds, one for each sensor, exception is the DHT11, which requires two feeds, one for temperature and one for humidity.
 * Instructions on how to set up feeds can be found on adafruits [basic-feeds tutorial](https://learn.adafruit.com/adafruit-io-basics-feeds).

## The Code
The code is divided into a few different files.  

* boot.py is the first script that runs when the Pico is powered up. It connects the machine to your wifi and sets up a connection to Adafruit.
* main.py basically consist of an endless loop of sending sensor values to the mqtt broker. 
* In the folder “lib/“ we got: 
	* mqtt.py - a library that lets us use the MQTT-protocol to send data to the broker
	* sensors.py - a library that connects ours sensors to the Raspberry Pi pico W and it holds functions to get the data from the sensors.
	* secrets.py - our credentials in a dictionary 

<p align='center'>
<img src='https://github.com/gurkwaan/baby_monitor_iot_project/blob/main/img/filetree.png?raw=true' width=400>
</p>

## Transmitting data
In this project we use WiFi and MQTT protocols to transmit data to adafruit. The data is transmitted every 3 seconds, this lets us get a "real-time" update within the scope of the free plan of Adafruit. 

## Presenting data
There we have it! 

To visualize this data, we will [set up a dashboard](https://learn.adafruit.com/adafruit-io-basics-dashboards) at adafruit using the four feeds we created.

The data that is stored in the database is:
	* Temp x 2 and humidity (only the latest read)
	* Sound is saved 4 hours.

<p align='center'>
<img src='https://github.com/gurkwaan/baby_monitor_iot_project/blob/main/img/dashboard.png' width=800>
</p>

## Final thoughts and design

This is a beginners to intermediate project in IoT. The setup is really basic, but the sound sensor provides a bit extra challenge, and it really doesn’t live up to my expectations.

To make it better,
* We can use a Raspberry Pi or an Arduino,
	So we can hook up a better (and calibrated) microphone. 
	Then we could use the KY-038 as a “wake-up sensor” and the other microphone could send sound data (so we can rule out sound that isn’t made by 		the baby)
* We could also change our way of sending data to Bluetooth, which would be more user friendly for this use case.
* Adding a vibration sensor would be neat as well.

<p align='center'>
<img src='https://github.com/gurkwaan/baby_monitor_iot_project/blob/main/img/final.jpg?raw=true' width=800>
</p>
