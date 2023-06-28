# boot.py -- run on boot-up
import network
import machine
from time import sleep
from lib.secrets import secrets


def do_connect():
    # Put modem on Station mode
    wlan = network.WLAN(network.STA_IF)

    # Check if already connected
    if not wlan.isconnected():
        print('connecting to network...')
        # Activate network interface
        wlan.active(True)
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(
            # Your WiFi Credential
            secrets["WIFI_SSID"],
            secrets["WIFI_PASS"])
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

def disconnect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    wlan.disconnect()
    wlan = None 

# WiFi Connection
try:
    ip = do_connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")