import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)

# set PWM freq to 50 Hz
servo = gpio.PWM(21, 50)
servo.start(2.5)

while True:

    # 90 deg
    servo.ChangeDutyCycle(12.5)
    time.sleep(1)

    # 0 deg
    servo.ChangeDutyCycle(7.5)
    time.sleep(1)

    # -90 deg
    servo.ChangeDutyCycle(2.5)
    time.sleep(1)