import RPi.GPIO as GPIO
import time

buzzer_pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)

pwm =GPIO.PWM(buzzer_pin,262)
pwm.start(10)

c=0

melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294, 392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]
try:
    for i in melody:
        c+=1
        pwm.ChangeFrequency(i)
        if c==7:
            time.sleep(1)
        if c==12:
            time.sleep(1)
        elif c==19:
            time.sleep(1)
        elif c==24:
            time.sleep(1)
        else:
            time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()
