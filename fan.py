import RPi.GPIO as GPIO
import time
import Adafruit_DHT #온습도센서 라이브러리 import
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11 #온습도 센서의 타입을 정해주는 sensor객체 생성
temp_pin = 13 #온습도센서 핀
B1A = 19 #모터 드라이브(l9110s)의 B1-A의 핀
B1B = 26 #모터 드라이브(l9110s)의 B1-B의 핀
 #쿨링 팬을 작동시킬 기준온도
#모터 드라이브 핀의 기초설정
GPIO.setup(B1A,GPIO.OUT)
GPIO.setup(B1B,GPIO.OUT)
GPIO.output(B1A,GPIO.LOW)
GPIO.output(B1B,GPIO.LOW)
def coolerfan(temp):
    while True:
        huminity, temperature = Adafruit_DHT.read_retry(sensor, temp_pin) #온습도센서에서 값을 받아옴
        if temperature > temp: #센서에서 받아온 온도가 쿨링 팬을 작동시킬 기준온도보다 높다면
            GPIO.output(B1A, GPIO.HIGH) #B1-A핀을 활성화 시킨다(B1-A는 정방향 회전)
            GPIO.output(B1B, GPIO.LOW) #B1-B는 역방향회전이기때문에 활성화 시키지 않는다
        else:
            GPIO.output(B1A, GPIO.LOW)
            GPIO.output(B1B, GPIO.LOW)
        time.sleep(0.5)
