import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

in1 = 13
in2 = 19
control = 25

gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)

gpio.setup(control, gpio.OUT)
controller = gpio.PWM(control, 50)

gpio.output(in1, gpio.LOW)
gpio.output(in2, gpio.LOW)

controller.start(75)

while True:
    
    inp = input('action: ')
    
    if inp == 'start':
        gpio.output(in1, gpio.LOW)
        gpio.output(in2, gpio.HIGH)
    
    elif inp == 'stop':
        gpio.output(in1, gpio.LOW)
        gpio.output(in2, gpio.LOW)