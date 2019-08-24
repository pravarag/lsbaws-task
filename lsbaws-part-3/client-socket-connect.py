import socket


# create socket and connect to server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))


# send and accept some data
sock.sendall(b'test message')
data = sock.recv(1024)
print(data.decode())

