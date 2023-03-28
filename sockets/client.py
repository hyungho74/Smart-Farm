# Import socket module
import socket


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
	while True:

		# message sent to server
		
		ans = input('\nput message(n:end socket) :')
		if ans == 'n':
			break
		else:
			s.send(ans.encode('utf-8'))
			data = s.recv(1024)
			print('Received from the server :',str(data.decode('utf-8')))
			continue
	# close the connection
	s.close()

if __name__ == '__main__':
	Main()
