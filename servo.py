import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

(trig, echo) = (18, 24)
gpio.setup(21, gpio.OUT)

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

# set PWM freq to 50 Hz
servo = gpio.PWM(21, 50)
servo.start(2.5)

def get_distance() -> float:

    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    st_pulse = time.time()
    en_pulse = time.time()

    while gpio.input(echo) == 0:
        st_pulse = time.time()

    while gpio.input(echo) == 1:
        en_pulse = time.time()

    duration = en_pulse - st_pulse
    distance = round((duration * 17150), 2)

    return abs(distance)


def set_servo_deg(target_deg: int) -> None:

    '''
        Set servo angle to target degree in range of 0-180 deg.
    '''

    set_deg = (target_deg - 0) * (12.5 - 2.5) / (180 - 0) + 2.5 if target_deg <= 180 else 100
    print(f'duty cycle = {set_deg} sec, deg = {target_deg}')
    servo.ChangeDutyCycle(set_deg)


print('Starting...')

gpio.output(trig, False)
print('Wait for sensor...')
time.sleep(1)

set_servo_deg(0)

while True:

    distance = 180 if int(get_distance()) > 180 else int(get_distance())
    
    print(f'Distance = {distance}')
    set_servo_deg(distance)

    time.sleep(0.3)