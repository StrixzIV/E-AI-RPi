import time 
import board
import adafruit_dht
import RPi.GPIO as gpio

import notifier

dhtSensor = adafruit_dht.DHT11(board.D4)

while True:
    
    try:

        c = dhtSensor.temperature
        f = (c * (9 / 5)) + 32

        humidity = dhtSensor.humidity

        print(f'Temp: {f:.1f}F / {c:.1f}C, Humidnity: {humidity}%')

        if c > 23:
            notifier.send_text_notification('[ALERT] Overheat detected')
            notifier.send_text_notification(f'Tempurature {c:.1f}C / {f:.1f}F, Humidnity: {humidity}%')

    except RuntimeError or OSError as e:

        dhtSensor.exit()
        
        print(e.args[0])
        time.sleep(2)

        continue

    except KeyboardInterrupt:
        dhtSensor.exit()
        print('Successfully exited.')

    time.sleep(2)
    gpio.cleanup()
