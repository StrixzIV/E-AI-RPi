import time
import RPi.GPIO as gpio


class UltrasonicSensor:

    '''
        A wrapper class for RaspberryPi ultrasonic sensor controller.
    '''

    def __init__(self, trig_pin: int, echo_pin: int):

        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)

        self.initialize()


    def initialize(self) -> None:
        
        '''
            Initializing ultrasonic sensor before running.
        '''
        
        print('Starting...')
        
        gpio.output(self.trig_pin, False)
        print('Wait for sensor...')
        
        time.sleep(1)


    def get_distance(self) -> float:
        
        '''
            Get distance from ultrasonic sensor.
        '''
        
        gpio.output(self.trig_pin, True)
        time.sleep(0.00001)
        gpio.output(self.trig_pin, False)

        start_pulse = time.time()
        end_pulse = time.time()

        while gpio.input(self.echo_pin) == 0:
            start_pulse = time.time()

        while gpio.input(self.echo_pin) == 1:
            end_pulse = time.time()

        duration = end_pulse - start_pulse
        distance = abs(round((duration * 17150), 2))

        return distance