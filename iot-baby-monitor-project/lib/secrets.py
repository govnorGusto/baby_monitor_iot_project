import ubinascii              # Conversions between binary data and various encodings
import machine


## NOTE 
# CHANGE THESE CREDENTIALS FOR YOUR SETUP

secrets = {
    # Wireless network
    "WIFI_SSID" : "Your WiFi ssid",
    "WIFI_PASS" : "the password to the wifi",

    # Adafruit IO (AIO) configuration
    "AIO_SERVER" : "io.adafruit.com", # The brokers adress
    "AIO_PORT" : 1883, # the port used to send the data
    "AIO_USER" : "your adafruit username",
    "AIO_KEY" : "your adafruit secret key",
    "AIO_CLIENT_ID" : ubinascii.hexlify(machine.unique_id()),  # Can be anything
    # Feeds usally builds "adafruit_username/feeds/specific_sensor" 
    "AIO_OUTSIDE_HUM_FEED" : "adafruit_username/feeds/dht11-hum-sensor",
    "AIO_OUTSIDE_TEMP_FEED" : "adafruit_username/feeds/dht11-temp-sensor",
    "AIO_BLANKET_TEMP_FEED" : "adafruit_username/feeds/blanket-temp",
    "AIO_ANALOG_SOUND_FEED" : "adafruit_username/feeds/ky038-analog-sound",
    "AIO_DIGITAL_SOUND_FEED" : "adafruit_username/feeds/ky038-digital-sound",
}
