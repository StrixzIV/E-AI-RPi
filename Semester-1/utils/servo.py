import time
import RPi.GPIO as gpio

class ServoMotor:

    '''
        A wrapper class for RaspberryPi servo controller.
    '''

    def __init__(self, servo_pin: int):
        self.servo_pin = servo_pin
        gpio.setup(self.servo_pin, gpio.OUT)


    def set_deg(self, target_deg: int, frequency: int = 50) -> None:

        '''
            Set servo angle to target degree in range of 0-180 deg.
        '''
        
        servo = gpio.PWM(self.servo_pin, frequency)
        servo.start(2.5)

        set_deg = (target_deg - 0) * (12.5 - 2.5) / (180 - 0) + 2.5 if target_deg <= 180 else 100
        print(f'duty cycle = {set_deg} sec, deg = {target_deg}')
        servo.ChangeDutyCycle(set_deg)


    def set_zero_deg(self):

        '''
            Set servo angle to 0 deg.
        '''

        self.set_deg(0)