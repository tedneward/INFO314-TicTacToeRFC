from argparse import ArgumentParser

TCP_PORT = 3116
UDP_PORT = 31161
TIMEOUT = 60 # The number of seconds to wait for a response from the server before timing out
LOGGING = 1 # 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
MAX_CLIENTS = 10

# Instantiate the argument parser
parser = ArgumentParser(description="Run a Tic-Tac-Toe server")

# Add arguments
parser.add_argument('-L', '--log-level', type=int, help='0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file', default=LOGGING)
parser.add_argument('-M', '--max-clients', type=int, default=MAX_CLIENTS)

def main():
	args = parser.parse_args()
	print(args.log_level)


if __name__ == "__main__":
	main()
