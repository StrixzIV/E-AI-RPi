import time
import RPi.GPIO as gpio

from utils import ultrasonic, servo

gpio.setmode(gpio.BCM)

(trig, echo) = (18, 24)

servo_motor = servo.ServoMotor(21)
ultrasonic_sensor = ultrasonic.UltrasonicSensor(trig, echo)

servo_motor.set_zero_deg()

while True:
    
    distance = ultrasonic_sensor.get_distance()
    angle = 180 if int(distance) > 180 else int(ultrasonic_sensor.get_distance())
    
    print(f'Distance = {distance}, Angle = {angle}')
    servo_motor.set_deg(21, angle)

    time.sleep(0.3)