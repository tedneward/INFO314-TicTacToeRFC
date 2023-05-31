from python_client.client import Client
import sys


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
