import time
from RPi import GPIO as gpio

btns = [19, 26]
relays = [20, 21]

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)

for btn in btns:
    gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)

for relay in relays:
    gpio.setup(relay, gpio.OUT)

while True:

    state1 = gpio.input(btns[0]) != 1
    state2 = gpio.input(btns[1]) != 1

    if state1:
        gpio.output(relays[0], False)
        gpio.output(relays[1], True)

    elif state2:
        gpio.output(relays[0], True)
        gpio.output(relays[1], False)

    else:
        gpio.output(relays[0], False)
        gpio.output(relays[1], False)

    time.sleep(0.5)