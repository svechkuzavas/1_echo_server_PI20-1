from socket import *
import sys
addr=('localhost', 9090)
udp_sock=socket(AF_INET, SOCK_DGRAM)

while True:
	data = input('text message to the server: ')
	data = str.encode(data)
	udp_sock.sendto(data, addr)
	data = bytes.decode(data)
udp_sock.close()
