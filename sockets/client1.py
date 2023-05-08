import socketio
import time

sio = socketio.Client()
@sio.event
def connect():
    print("connect")

@sio.event
def connect_error():
    print("connect_error")
    
@sio.event
def disconnect():
    print("disconnect")

sio.connect('http://localhost:8070')
print("my sid is",sio.sid)

while(1):
     sio.emit('msssage', {'foo' : 'bar'})
     print("tlqkf")
     time.sleep(1)
