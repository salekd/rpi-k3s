import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.OUT)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    gpio.output(26, gpio.HIGH)
    time.sleep(0.2)
    gpio.output(26, gpio.LOW)

    return req
