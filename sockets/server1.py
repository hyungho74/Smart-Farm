# import socket programming library
import socket
import time
# import thread module
from _thread import *
import threading
import select

print_lock = threading.Lock()
# thread function
def threaded(c):
	while True:
		text = 'hello'
		text = text.encode('utf-8')
		# data received from client
		data = c.recv(1024)
		if not data:
			print('Bye')
			# lock released on exit
			print_lock.release()
			break

		# reverse the given string from client
		data = data[::-1]

		# send back reversed string to client
		c.send(data)

	# connection closed
	c.close()

def thread1(c):
	while True:
		print_lock.acquire()
		text = 'hi'
		text = text.encode('utf-8')
		# data received from client
		c.send(text)
		print_lock.release()
		time.sleep(2)
	# connection closed
	c.close()
	
def thread2(c):
	while True:
		print_lock.acquire()
		data = c.recv(1024)
		c.send(data)
		print_lock.release()
		time.sleep(2)
	# connection closed
	c.close()

def thread3(c):
	while True:
		print_lock.acquire()
		data = c.recv(1024)
		c.send(data)
		print_lock.release()
		time.sleep(1)
	# connection closed
	c.close()

def Main():
	
	host = "10.82.17.194"

	# reserve a port on your computer
	# in our case it is 12345 but it
	# can be anything
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	s.listen(5)
	print("socket is listening")

	# a forever loop until client wants to exit
	while True:

		# establish connection with client
		c, addr = s.accept()

		# lock acquired by client
		print('Connected to :', addr[0], ':', addr[1])

		# Start a new thread and return its identifier
		start_new_thread(thread3, (c,))
	s.close()


if __name__ == '__main__':
	Main()
