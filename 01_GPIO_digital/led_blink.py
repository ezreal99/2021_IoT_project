import RPi.GPIO as GPIO
import time

LED_PIN1 = 17
LED_PIN2 = 4
LED_PIN3 = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)
GPIO.setup(LED_PIN3,GPIO.OUT)

for i in range(1):
    GPIO.output(LED_PIN1,GPIO.HIGH)
    print('LED ON')
    time.sleep(2)
    GPIO.output(LED_PIN1,GPIO.LOW)
    print('LED OFF')
    GPIO.output(LED_PIN2,GPIO.HIGH)
    print('LED ON')
    time.sleep(2)
    GPIO.output(LED_PIN2,GPIO.LOW)
    print('LED OFF')
    GPIO.output(LED_PIN3,GPIO.HIGH)
    print('LED ON')
    time.sleep(2)
    GPIO.output(LED_PIN3,GPIO.LOW)
    print('LED OFF')

GPIO.cleanup()