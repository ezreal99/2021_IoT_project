import cv2
import RPi.GPIO as GPIO
import time
import pigpio

SWITCH_PIN = 25
PIR_PIN = 4
BUZZER_PIN = 18
#PIN 세팅

GPIO.setmode(GPIO.BCM) 
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN,GPIO.LOW)
#GPIO 세팅

pi=pigpio.pi()
pi.set_servo_pulsewidth(19,0)
#서보모터 세팅
print("Loading ..")
time.sleep(1)

cap = cv2.VideoCapture(0)

if not cap.isOpened(): #카메라가 닫혀있으면 종료
     print('Camera open failed')
     exit()
try:
    while True:
        ret, frame = cap.read()
        if not ret:
           break
        cv2.imshow('frame', frame) #카메라 재생

        val = GPIO.input(SWITCH_PIN)
        val2 = GPIO.input(PIR_PIN)
        #SWITCH, PIR 입력받기

        if val == 0: #스위치가 눌리면 서보모터 작동
            pi.set_servo_pulsewidth(19,550) 
            time.sleep(1)
            pi.set_servo_pulsewidth(19,1500)

        if val2 == 1: #PIR센서에 감지되면
            GPIO.output(BUZZER_PIN,GPIO.HIGH) #BUZZER ON
            print("buzzer on")
        else:
            GPIO.output(BUZZER_PIN,GPIO.LOW) #BUZZER OFF
            print("buzzer off")    

        if cv2.waitKey(10) == 13:
            break
finally:
    GPIO.cleanup()
    cap.release()
    cv2.destoryAllWindows()