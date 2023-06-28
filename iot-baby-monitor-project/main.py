import time
from lib import sensors
from lib.secrets import secrets
from lib.mqtt import MQTTClient
from boot import disconnect


def send_payload(sensor_value,feed):
    """publish a payload to adafruit IO"""
    print("Publishing: {0} to {1} ... ".format(sensor_value, feed), end='')
    try:
        client.publish(topic=feed, msg=str(sensor_value))
        print("DONE")
    except Exception as e:
        print("FAILED")


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(
    secrets["AIO_CLIENT_ID"],
    secrets["AIO_SERVER"],
    secrets["AIO_PORT"],
    secrets["AIO_USER"],
    secrets["AIO_KEY"])
client.connect()
print("Connected to %s" % (secrets["AIO_SERVER"]))

# the time.sleep() is implemented because of free account at io.adafruit.com
free_adafruit_timer = time.sleep(4)
try:
    while True:
        # Send a digital sound to Adafruit IO.
        time.sleep(3)
        send_payload(
            sensor_value=sensors.read_ky038()[1],
            feed=secrets["AIO_DIGITAL_SOUND_FEED"]
        )
        # doesn't allow too much data per minute/
        time.sleep(3)
        # Send a analog temp to Adafruit IO.
        send_payload(
            sensor_value=sensors.read_analog_temp(),
            feed=secrets["AIO_BLANKET_TEMP_FEED"]
            )
        # Send a digital sound to Adafruit IO.
        time.sleep(3)
        send_payload(
            sensor_value=sensors.read_ky038()[1],
            feed=secrets["AIO_DIGITAL_SOUND_FEED"]
        )
        time.sleep(3)
        # Send a DHT11 temp to Adafruit IO.
        send_payload(
            sensor_value=sensors.read_dht11()[1],
            feed=secrets["AIO_OUTSIDE_TEMP_FEED"]
            )
        # Send a digital sound to Adafruit IO.
        time.sleep(3)
        send_payload(
            sensor_value=sensors.read_ky038()[1],
            feed=secrets["AIO_DIGITAL_SOUND_FEED"]
        )
        time.sleep(3)
        # Send a DHT hum to Adafruit IO.
        send_payload(
            sensor_value=sensors.read_dht11()[0],
            feed=secrets["AIO_OUTSIDE_HUM_FEED"])

# If an exception is thrown
# disconnect the client and clean up.
finally:
    client.disconnect()
    client = None
    disconnect()
    print("Disconnected from Adafruit IO.")