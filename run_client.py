# Import the Client class
import sys
from engine.client import Client
from argparse import ArgumentParser
from engine.helpers import prt_dbg
from engine import *


parser = ArgumentParser(description="Client program for connecting to the server.")

parser.add_argument('-CT', '--connection-type', type=str, help='The type of connection to use. Either TCP or UDP.', default="TCP")
parser.add_argument('-H', '--hostname', type=str, help='The hostname of the server to connect to.', default="localhost")
parser.add_argument('-L', '--log-level', type=int, help='0 = No logging, 1 = Log to console', default=1)

def main():
	try:
		args = parser.parse_args()
		connection_type = args.connection_type
		hostname = args.hostname
		log_level = args.log_level
		# Create a client
		client = Client(connection_type, hostname, log_level)
		if type(client) == Client:
			prt_dbg("Client created successfully", LOGGING)
		else:
			prt_dbg("Client creation failed", LOGGING)
		while True:
			text = input("\n")
			# print(text)
			client.send_message(text)
	except KeyboardInterrupt:
		prt_dbg("Keyboard interrupt detected. Exiting...", LOGGING)
		sys.exit(0)
	except Exception as e:
		prt_dbg(str(e), 1)
		sys.exit(1)

if __name__ == "__main__":
	main()
