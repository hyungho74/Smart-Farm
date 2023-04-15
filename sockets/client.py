# Import socket module
import socket
import time

def Main():
	# local host IP '127.0.0.1'
    host = '10.82.17.194'

    # Define the port on which you want to connect
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    s.connect((host,port))
    # message you send to server
    message = "hello"
    message1 = "hi"
    s.send(message.encode('utf-8'))
    while True:
        data = s.recv(1024)
        data = str(data.decode('utf-8'))
        print('Received from the server :',data)
        if data == 'hello':
            s.send(message1.encode('utf-8'))
        else:
            s.send(message.encode('utf-8'))
        time.sleep(1)

if __name__ == '__main__':
	Main()
