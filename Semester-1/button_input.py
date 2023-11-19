import RPi.GPIO as gpio
import time 

(btn, led) = (13, 26)

gpio.setmode(gpio.BCM)
gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(led, gpio.OUT)

while True:

    state = gpio.input(btn) == 1

    if state:
        print('Pressed')

    else:
        print('Release')


    time.sleep(0.3)
