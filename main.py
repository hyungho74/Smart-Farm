import pymysql,time
from flask import Flask, render_template, render_template_string,Request,request, Response
from water import water
from pump import waterpump
from fan import coolerfan
from light import light
from cam import gen
app = Flask(__name__)
conn = pymysql.Connect(host='10.82.17.194', user = 'rasp', password = 'password', db = 'database', charset = 'utf8') 
curr = conn.cursor()
sql = "insert into value1 value ('1', 'test', '성공')"
conn.commit()
curr.clost()
conn.close()
conn = None
curr = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor', methods = ['POST'])
def sensor():
    return

@app.route('/video_feed', methods = ['GET'])
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')