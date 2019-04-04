import argparse
import xmlrpclib
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer

# some trivial functions

def add(x,y):
	return x+y
def subtract(x, y):
	return x-y
def multiply(x, y):
	return x*y
def divide(x, y):
	return x/y
class ServerThread(threading.Thread):
	def __init__(self, server_addr):
		threading.Thread.__init__(self)
		self.server = SimpleXMLRPCServer(server_addr)
		self.server.register_multicall_functions()
		self.server.register_function(add, 'add')
		self.server.register_function(subtract, 'subtract')
		self.server.register_function(multiply, 'multiply')
		self.server.register_function(divide, 'divide')
	def run(self):
		self.server.serve_forever()

def run_server(host, port):
	# server code
	server_addr = (host, port)
	server = ServerThread(server_addr)
	server.start() # The server is now running
	print "Server thread started. Testing the server..."
def run_client(host, port):
	# client code
	proxy = xmlrpclib.ServerProxy("http://%s:%s/" %(host, port))
	multicall = xmlrpclib.MultiCall(proxy)
	multicall.add(10,5)
	multicall.subtract(10,5)
	multicall.multiply(10,5)
	multicall.divide(10,5)
	result = multicall()
	print "10+5=%d, 10-5=%d, 10*5=%d, 10/5=%d" % tuple(result)
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Multithreaded multicall XMLRPC Server/Proxy')
	parser.add_argument('--host', action="store", dest="host", default='localhost')
	parser.add_argument('--port', action="store", dest="port", default=8000, type=int)
	# parse arguments
	given_args = parser.parse_args()
	host, port = given_args.host, given_args.port
	run_server(host, port)
	run_client(host, port)

