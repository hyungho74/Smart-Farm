import Adafruit_DHT      # 라이브러리 불러오기 [sudo pip install Adafruit_DHT]

sensor = Adafruit_DHT.DHT11     #  센서의 타입을 정해주는 sersor객체 생성(DHT22/AM2302를 사용하면 Adafruit_DHT.DHT22/Adafruit_DHT.AM2302를 사용)

pin = 2                 #BOARD가 아닌, BCM의 핀 넘버를 사용       

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)   # 센서 객체에서 센서 값(온도, 습도) 읽기

while True:
    if humidity is not None and temperature is not None:   #습도 및 온도 값이 모두 제대로 읽혔다면 
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  
    else:                                                   
        print('Error')   