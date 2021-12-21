from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 26
#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#라우팅을 위한 뷰 함수
@app.route("/")
def hello_world():
    return '''
    <h1>Hello, Flask</h1>
    <a href = "/led/on"><h1>LED ON</h1></a>
    <a href = "/led/off"><h1>LED OFF</h1></a>
    '''
@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
        <h1>LED ON</h1>
        <a href="/"><h1>Go Home</h1></a>
        '''
    elif op =="off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
        <h1>LED OFF</h1>
        <a href="/"><h1>Go Home</h1></a>
        '''

#터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()