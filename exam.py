import time
import turtle
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

(led1, led2) = (20, 21)
btn = 18

gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)

gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(12, gpio.OUT)
servo = gpio.PWM(12, 50)

servo.start(2.5)

def set_servo_deg(target_deg: int) -> None:

    '''
        Set servo angle to target degree in range of 0-180 deg.
    '''

    set_deg = (target_deg - 0) * (12.5 - 2.5) / (180 - 0) + 2.5 if target_deg <= 180 else 100
    print(f'duty cycle = {set_deg} sec, deg = {target_deg}')
    servo.ChangeDutyCycle(set_deg)
    

set_servo_deg(90)

led_state = True

while True:

    state = not (True if gpio.input(btn) == 1 else False)

    if state:

        gpio.output(led1, led_state)
        gpio.output(led2, not led_state)

        set_servo_deg(0)

        time.sleep(0.4)

        set_servo_deg(180)

        led_state = not led_state
        

    else: 
        counter = 0
        gpio.output(led1, False)
        gpio.output(led2, False)
        set_servo_deg(90)

    time.sleep(0.3)
