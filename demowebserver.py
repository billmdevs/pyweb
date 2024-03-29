import os
import time
import socket

SERVER_ADDRESS = (HOST, PORT) = "", 7777
REQUEST_SIZE_QUEUE = 5

def handle_request(client_connection):
	request = client_connection.recv(1024)
	print(
		"Child PID: {pid}. Parent PID {ppid}".format(
			pid=os.getpid(),
			ppid=os.getppid()
		)
	)
	print(request.decode())
	http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
	client_connection.sendall(http_response)
	time.sleep(60)


def serve_forever():
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listen_socket.bind(SERVER_ADDRESS)
	listen_socket.listen(REQUEST_SIZE_QUEUE)
	print("Serving HTTP on port {PORT} ...")
	print("Parent PID (PPID): {pid}\n".format(pid=os.getpid()))
	while True:
		client_connection, client_address = listen_socket.accept()
		pid = os.fork()
		if pid == 0: # child process
			listen_socket.close()
			handle_request(client_connection)
			client_connection.close()
			os._exit(0)
		else: # parent process
			client_connection.close() # close parent copy and loop over
			# print(len(clients))

if __name__ == "__main__":
	serve_forever()
