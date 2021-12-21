import RPi.GPIO as GPIO
import time

pir_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin,GPIO.IN)

time.sleep(5)
print('pir ready...')

try:
    while True:
        val = GPIO.input(pir_pin)
        if val==1:
            print('움직임 감지')
        else:
            print('움직임 없음')
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')