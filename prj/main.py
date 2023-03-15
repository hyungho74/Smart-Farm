from flask import Flask, render_template, render_template_string, Response, request
from servo import current_deg, set_servo_degree, set_servo_degree1
from cam import gen
app = Flask(__name__)
set_servo_degree(current_deg)
set_servo_degree1(current_deg)
@app.route('/')
def index():
    return render_template('index.html', deg=current_deg, deg1=current_deg)

@app.route('/servo_control')
def servo_control():
    deg = request.args.get('deg') #html파일에서 각도를 입력받음
    deg = int(deg) #각도를 정수형으로 바꿔주고 적절한 범위로 바꿔줌
    if deg < 0:
        deg = 0
    elif deg > 180:
        deg = 180
    deg = set_servo_degree(deg)
    deg1 = request.args.get('deg1') #html파일에서 각도를 입력받음
    deg1 = int(deg1) #각도를 정수형으로 바꿔주고 적절한 범위로 바꿔줌ㅁ
    if deg1 < 0:
        deg1 = 0
    elif deg1 > 180:
        deg1 = 180
    deg1 = set_servo_degree(deg1)
    return render_template('index.html', deg = deg, deg1 = deg1)

@app.route('/   video_feed', methods = ['GET'])
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ =="__main__":
    app.run(host="0.0.0.0", port="8000")