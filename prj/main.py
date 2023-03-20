import time
from flask import Flask, render_template, render_template_string, request, Response
from water import watersensor,sqlwater
from pump import waterpump, sqlpump
from fan import coolerfan, sqlfan
from light import lightsensor, sqllight
from cam import gen

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/sensor', methods = ['POST'])
def sensor():
	global temp
	global hum
	temp = request.form['temp']
	hum = request.form['hum']   
	return render_template('manage.html', temp = temp, hum = hum)
	
	
@app.route('/video_feed', methods = ['GET'])
def video_feed():
	return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
	
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8000")
	