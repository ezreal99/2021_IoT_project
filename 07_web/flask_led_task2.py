from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN1 = 21
LED_PIN2 = 26
#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

#라우팅을 위한 뷰 함수
@app.route("/")
def hello_world():
    return render_template("led2.html")
@app.route("/led/<op>")
def led_op(op):
    if op == "redon":
        GPIO.output(LED_PIN1, GPIO.HIGH)
        return "RED LED ON"
    elif op =="redoff":
        GPIO.output(LED_PIN1, GPIO.LOW)
        return "RED LED OFF"
    elif op =="blueon":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "BLUE LED ON"
    elif op =="blueoff":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "BLUE LED OFF"
    else:
        return "Error"

#터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()