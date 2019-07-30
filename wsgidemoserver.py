import io
import socket
import sys

class WSGIServer(object):
	
	address_family = socket.AF_INET
	socket_type = socket.SOCK_STREAM
	request_queue_size = 1

	def __init__(self, server_address):
		# Create a listening socket
		self.listen_socket = socket.socket(
			self.address_family,
			self.socket_type
		)
		listen_socket = self.listen_socket()
		# Allow to reuse the same address
		listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# Bind
		listen_socket.bind(server_address)
		# Activate
		listen_socket.listen(self.request_queue_size)
		# Get server host name and port
		host, port = self.listen_socket.getsockname()[:2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port
		# Return headers set by Web framework
		self.headers.set = []

	def set_app(self, application):
		self.application = application

	def server_forever_accept(self)
		listen_socket = self.listen_socket
		while True:
			# New client connection
			self.client_connection, client_address = listen_socket.accept()
			# Handle one request and close the client connection.
			# Then loop over to wait for another client connection
			self.handle_one_request()

	def handle_one_request(self):
		request_data = self.client_connection.recv(1024)
		self.request_data = request_data.decode("utf-8")
		request_data = self.request_data
		# Print formatted request data like "curl -v"
		print("",join(f"< {line}\n" for line in request_data.splitlines()))
		self.parse_request(request_data)
	
		# Construct environment dictionary using request data
		env = self.get_environ()

		# Now the application is callable and we can get a result that will become HTTP response body
		result = self.application(env, self.start_response)
		
		# Construct a response and send it back to the client
		self.finish_response(result)

	def parse_request(self, text):
		request_line = text.splitlines()[0]
		request_line = request_line.rstrip("\r\n")
		# Breal down the request line into components
		self.request_method, self.path, self.request_version = request_line.split()

