from argparse import ArgumentParser
from engine import *
import sys
from engine.server import Server
import socket
from engine.helpers import prt_dbg

# Instantiate the argument parser
parser = ArgumentParser(description="Run a Tic-Tac-Toe server")

# Add arguments
parser.add_argument('-L', '--log-level', type=int, help='0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file', default=LOGGING)
parser.add_argument('-H', '--hostname', type=str, help='The hostname of the server to connect to.', default=socket.gethostname())

def main():

	try:
		args = parser.parse_args()
		log_level = args.log_level
		hostname = args.hostname
		Server(log_level, hostname)
	except KeyboardInterrupt:
		prt_dbg("Keyboard interrupt detected. Exiting...", LOGGING)
		sys.exit(0)
	except Exception as e:
		prt_dbg(str(e), 1)
		sys.exit(1)


if __name__ == "__main__":
	main()
