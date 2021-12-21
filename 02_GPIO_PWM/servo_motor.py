import RPi.GPIO as GPIO

servor_motor_pin=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servor_motor_pin,GPIO.OUT)

pwm = GPIO.PWM(servor_motor_pin,50)
pwm.start(7.5) #각도 조절

try:
    while True:
        val = input('1: 0도, 2: -90도, 3: 90도, 9:exit >')
        if val=='1':
            pwm.ChangeDutyCycle(7.5)
        elif val=='2':
            pwm.ChangeDutyCycle(5)
        elif val=='3':
            pwm.ChangeDutyCycle(10)
        elif val=='9':
            break

finally:
    pwm.stop()
    GPIO.cleanup()