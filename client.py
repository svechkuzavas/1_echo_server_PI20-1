import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))
msg=''
while msg != 'close':
	msg = input('Your message: ')
	sock.send(msg.encode())
	data = sock.recv(1024)
sock.close()
