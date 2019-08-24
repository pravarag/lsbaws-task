import os
import socket
import time


server_address = (HOST, PORT) = '', 8888
request_queue_size = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    pid = os.getpid()
    ppid = os.getppid()
    print(f'Child PID: {pid}. Parent PID {ppid}')
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    time.sleep(60)


def serve_forever():
    listen_socket = socket.socket(socket.ATF_INET, socket.SOCK_STREAM)
    listen_socket.sockopt(socket.SOL_SOCKE, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    pid = os.getpid()
    print(f'Serving HTTP on port {PORT}')
    print(f'Parent PID {pid}\n')

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()

if __name__ == '__main__':
    serve_forever()
