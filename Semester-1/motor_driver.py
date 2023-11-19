import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

in1 = 16
in2 = 21
control = 25
btns = (5, 6, 13)

base_speed = 30

for btn in btns:
    gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)

gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)

gpio.setup(control, gpio.OUT)
controller = gpio.PWM(control, 50)

controller.start(0)

while True:
    
    (state1, state2, state3) = (not gpio.input(btns[0]), not gpio.input(btns[1]), not gpio.input(btns[2]))

    print(f'state1: {state1}, state2: {state2} state3: {state3}, speed: {base_speed}')

    if state1:
        controller.ChangeDutyCycle(base_speed)
        gpio.output(in1, gpio.HIGH)
        gpio.output(in2, gpio.LOW)
    
    elif state2:
        print('state2')
        controller.ChangeDutyCycle(base_speed)
        gpio.output(in1, gpio.LOW)
        gpio.output(in2, gpio.HIGH)

    elif state3:

        if base_speed >= 100:
            base_speed = 30

        else:
            base_speed += 10
    else:
        controller.ChangeDutyCycle(0)
        gpio.output(in1, gpio.LOW)
        gpio.output(in2, gpio.LOW)

    time.sleep(0.1)