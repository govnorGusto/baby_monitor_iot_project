import dht
import time
from machine import Pin, ADC

# Pin Setup
# ---------

# DHT11
dht11_sensor = dht.DHT11(Pin(16))
# MCP9700 Analog thermistor
analog_temp_sensor = ADC(26)

# KY-038
# Analog pin
analog_sound_sensor = ADC(27)
# Digital pin connected to the DO pin of KY-038
digital_sound_sensor = Pin(28, Pin.IN)

def read_analog_temp():
    """
    Reads analog value and converts it to degrees in celcius.
    Returns the temperature rounded by 2 decimals.
    """
    millivolts = analog_temp_sensor.read_u16()
    sf = 4095 / 65535  # Scale factor
    volt_per_adc = 3.3 / 4095
    adc_12b = millivolts * sf
    volt = adc_12b * volt_per_adc
    # MCP9700 characteristics
    dx = abs(50 - 0)
    dy = abs(0 - 0.5)
    shift = volt - 0.5
    temp = shift / (dy / dx)
    return round(temp,2)
    # for debug
    # print(f"Analog temperature is {round(temp,2)} degrees Celsius") 

def read_dht11():
    """
    Reads the DHT11 sensor
    Returns a tuple: (humidity, temperature)
    """
    dht11_sensor.measure()
    temp = dht11_sensor.temperature()
    hum = dht11_sensor.humidity()
    # for debug
    # print(f"Temperature is {temp} degrees Celsius")
    # print(f"Humidity is {hum}%")
    return hum,temp

def read_ky038():
    """
    Reads the KY-038 sound sensor
    Returns a tuple (analog_value, digital_value)
    """
    analog_value = analog_sound_sensor.read_u16()
    digital_value = digital_sound_sensor.value()

    # The analog_value of ~ 33333 is circa normal speaking volume (around 60 dB)
    # the threshold for the digital output (0 or 1)  will be around there
    # this is calibrated on the potentiometer on the KY-038
    # to set the analog value of 33333 to ca 45% i floor divided by 740

    return analog_value, digital_value