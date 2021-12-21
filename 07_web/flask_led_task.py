from flask import Flask
import RPi.GPIO as GPIO

LED_PIN1 = 26
LED_PIN2 = 13
#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

#라우팅을 위한 뷰 함수
@app.route("/")
def hello_world():
    return '''
    <h1>Hello, Flask</h1>
    <a href = "/led/red/on"><h1>RED LED ON</h1></a>
    <a href = "/led/red/off"><h1>RED LED OFF</h1></a>
    <a href = "/led/blue/on"><h1>BLUE LED ON</h1></a>
    <a href = "/led/blue/off"><h1>BLUE LED OFF</h1></a>
    '''
@app.route("/led/<op1>/<op2>")
def led_op(op1,op2):
    if op1 == "red":
        if op2 == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return '''
            <h1>RED LED ON</h1>
            <a href="/"><h1>Go Home</h1></a>
            '''
        elif op2 == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return '''
            <h1>RED LED OFF</h1>
            <a href="/"><h1>Go Home</h1></a>
            '''
    elif op1 =="blue":
        if op2 == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return '''
            <h1>BLUE LED ON</h1>
            <a href="/"><h1>Go Home</h1></a>
            '''
        elif op2 == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return '''
            <h1>BLUE LED OFF</h1>
            <a href="/"><h1>Go Home</h1></a>
            '''
        

#터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()