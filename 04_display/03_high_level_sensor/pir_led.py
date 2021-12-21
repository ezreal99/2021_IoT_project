import RPi.GPIO as GPIO
import time

pir_pin = 4
led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

time.sleep(5)
print('pir ready...')

try:
    while True:
        val = GPIO.input(pir_pin)
        if val==1:
            print('움직임 감지')
            GPIO.output(led_pin,GPIO.HIGH)
        else:
            print('움직임 없음')
            GPIO.output(led_pin,GPIO.LOW)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')