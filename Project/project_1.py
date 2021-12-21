import RPi.GPIO as GPIO
import time

led_pin = 6
trigger_pin = 17
echo_pin = 12           
pir_pin = 4
buzzer_pin = 5
# pin 번호 설정

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)
GPIO.setup(pir_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(buzzer_pin,GPIO.OUT)
# GPIO 세팅

pwm =  GPIO.PWM(buzzer_pin,262)

try:
    while True:
        GPIO.output(trigger_pin,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger_pin,GPIO.LOW)
        val = GPIO.input(pir_pin) # pir 센서로 감지
        while GPIO.input(echo_pin)==0:
                pass
        start = time.time()
        while GPIO.input(echo_pin)==1:
                pass
        stop = time.time()
        d_time = stop-start
        d=17160*d_time # 초음파 센서로 거리(cm) 측정
        if val == 1 and d<=50: # 앞에 사람이 있고 거리가 50cm 미만이면
            pwm.start(10)
            GPIO.output(led_pin,GPIO.HIGH) # led on
            pwm.ChangeFrequency(440) # buzzer on
            print('Warning! Distance : %.1fcm'%d)
        else:
            GPIO.output(led_pin,GPIO.LOW) # led off
            pwm.stop() # buzzer                                 off
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')