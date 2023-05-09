import time
import requests
import socketio


# Socket.IO 클라이언트 생성
sio = socketio.Client()

# Socket.IO 이벤트 핸들러
@sio.event
def connect():
    print('Socket.IO 서버에 연결되었습니다.')

@sio.event
def disconnect():
    print('Socket.IO 서버와 연결이 끊어졌습니다.')

# 데이터 전송 함수
def send_sensor_data(data):
    # Socket.IO 서버로 데이터 전송
    sio.emit('sensor_data', data)
    print('센서 데이터 전송:', data)

# 측정 함수
def read_sensor_values():
    # 온습도 센서(DHT11) 읽기
    temperature = 23
    humidity = 18
    light = 100

    # 수위 센서 읽기
    water_level = 90

    # 토양 습도 센서 읽기
    soil_moisture = 60

    # 센서 데이터 반환
    sensor_data = {
        'temperature': temperature,
        'humidity': humidity,
        'light': light,
        'water_level': water_level,
        'soil_moisture': soil_moisture
    }
    return sensor_data

# Socket.IO 서버에 연결
sio.connect('http://localhost:3000')

# 주기적으로 센서 값을 읽고 전송
while True:
    try:
        sensor_data = read_sensor_values()
        send_sensor_data(sensor_data)
        time.sleep(10)  # 10초마다 측정 및 전송
    except KeyboardInterrupt:
        break

# Socket.IO 클라이언트 연결 종료
sio.disconnect()
