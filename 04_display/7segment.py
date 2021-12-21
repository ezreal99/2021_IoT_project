import RPi.GPIO as GPIO
import time

seg_pin = [2,3,4,5,6,7,8]

GPIO.setmode(GPIO.BCM)

for i in seg_pin:
    GPIO.setup(i,GPIO.OUT)
    GPIO.setup(i,GPIO.LOW)

data = [1,1,1,1,1,1,0]

try:
    for _ in range(3):
        for i in range(7):
            GPIO.output(seg_pin[i],data[i])
        time.sleep(1)
        for i in range(7):
            GPIO.output(seg_pin[i],GPIO.LOW)

finally:
    