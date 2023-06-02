# Import the Client class
import sys
from engine.client import Client
from argparse import ArgumentParser


parser = ArgumentParser(description="Client program for connecting to the server.")


def main():
	try:

		# Parse command line arguments
		cmd_args = sys.argv[1:]
		print(cmd_args)

		# Create a client
		client = Client()
		if type(client) == Client:
			print("Client created successfully")
			print("Enter the protocol, followed by either \"start\" or the six-character game code")
		else:
			sys.exit("Client creation failed")
	except KeyboardInterrupt:
		sys.exit("Goodbye")
	except Exception as _:
		sys.exit("An error occurred")

if __name__ == "__main__":
	main()
