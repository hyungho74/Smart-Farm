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

@sio.event
def chat_message(data):
    print('새로운 메시지:', data)

# Socket.IO 서버에 연결
sio.connect('http://localhost:8070')

# 채팅 입력 및 전송
while True:
    message = input('메시지를 입력하세요 (나가기: q): ')
    if message == 'q':
        break
    sio.emit('chat_message', message)

# Socket.IO 클라이언트 연결 종료
sio.disconnect()
