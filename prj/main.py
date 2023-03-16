import pymysql,time
from flask import Flask, render_template, render_template_string, request, Response
from water import watersensor,sqlwater
from pump import waterpump, sqlpump
from fan import coolerfan, sqlfan
from light import lightsensor, sqllight
from cam import gen

app = Flask(__name__)
conn = pymysql.Connect(host='10.82.17.194', user = 'rasp', password = 'kim8213!!' db = '', charset = 'utf8')
curr = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/sensor', methods = ['POST'])
def sensor():
	temp = request.form['temp']
	hum = request.form['hum']
	water = sqlwater()
	soil = sqlpump()
	temper,humin = sqlfan()
	light = sqllight()
	sql = "insert into smartfarm value (\'"+ temper +"\',\'"+ humin +"\',\'"+ soil +"\',\'"+ light +"\',\'"+ water +"\')"
	conn.commit()
	curr.close()
	conn.close()
	conn = None
	conn = None
	return render_template('manage.html', temp = temp, hum = hum)
	
	
@app.route('/video_feed', methods = ['GET'])
def video_feed():
	return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
	
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8000")