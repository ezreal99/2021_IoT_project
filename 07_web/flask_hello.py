from flask import Flask

#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)

#라우팅을 위한 뷰 함수
@app.route("/")
def hello_world():
    return '''
    <h1>Hello, Flask</h1>
    <a href = "/led/on"><h1>LED ON</h1></a>
    <a href = "/led/off"><h1>LED OFF</h1></a>
    '''

@app.route("/led/on")
def first():
    return '''
    <h1>LED ON</h1>
    <a href="/"><h1>Go Home</h1></a>
    '''

@app.route("/led/off")
def second():
    return '''
    <h1>LED OFF</h1>
    <a href="/"><h1>Go Home</h1></a>
    '''
    

#터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")