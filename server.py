from socket import *

addr = ('localhost', 9090)
clients = []
print('[server started...]')
udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(addr)
while True:
	data, address = udp_sock.recvfrom(1024)
	if not address in clients:
		clients.append(address)
		print('[new client added...]')
	for client in clients:
		if client == address:
			udp_sock.sendto(data, client)
			print(f"[message by {client}]{bytes.decode(data)}")
