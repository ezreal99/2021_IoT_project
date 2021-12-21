import RPi.GPIO as GPIO
import time

buzzer_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)

pwm =GPIO.PWM(buzzer_pin,262)
pwm.start(10)

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()
