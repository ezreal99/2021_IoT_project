import RPi.GPIO as GPIO
import time

trigger_pin = 4
echo_pin = 17
led_pin = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

try:
    while True:
        GPIO.output(trigger_pin,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger_pin,GPIO.LOW)
        while GPIO.input(echo_pin)==0:
            pass
        start = time.time()
        while GPIO.input(echo_pin)==1:
            pass
        stop = time.time()
        d_time = stop-start
        d=17160*d_time
        if d<=20:
            GPIO.output(led_pin,GPIO.HIGH)
            print('led ON')
        else:
            GPIO.output(led_pin,GPIO.LOW)
            print('led off')
        print('Distance : %.1fcm'%d)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')