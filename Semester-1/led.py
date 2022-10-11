import time
from RPi import GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)

while True:

    gpio.output(21, True)
    time.sleep(0.1)

    gpio.output(21, False)
    time.sleep(0.1)


