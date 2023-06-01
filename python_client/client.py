# This is a Client for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the server.
from tkinter import *
import socket
import threading
import uuid
import sys          # Use sys.argv to get command line arguments
import atexit       # For sending the server a "quit" message when the client is closed


class Client:
	def __init__(self):
		self.id = uuid.uuid4().hex
		self.running = False
		self.version = 0     # Should be 1 or 2
		self.protocol = None
		self.game_code = None
		self.window_title = "Tic-Tac-Toe Client"

		self.game_id = None

		# Start the GUI on the main thread
		self._start()

		# Start the keyboard input handler in a separate thread
		# keyboard_input_thread = threading.Thread(target=self._handle_keyboard_input)
		# keyboard_input_thread.start()

	def _start(self):
		"""
		Set up the GUI window and start the client
		"""
		# Create the main window
		window = Tk(screenName=self.window_title)
		window.title(self.window_title)

		# Create a label
		window_title_label = Label(window, text="Tic-Tac-Toe Client")

		# Place the label where there is space
		window_title_label.pack()

		# # Create a start-game button
		# start_game_button = Button(window, text="Start Game")
		#
		# # Create a restart-game button
		# restart_game_button = Button(window, text="Restart Game")
		#
		# # Create an "Enter Game Code" label
		# enter_game_code_label = Label(window, text="Enter Game Code")
		#
		# # Create a text-entry field for the game code
		# game_code_entry = Entry(window)

		# Let's make the default window dimensions half the screen width and half the screen height
		screen_width = window.winfo_screenwidth() / 2
		screen_height = window.winfo_screenheight() / 2

		# Adjust the window size
		window.geometry(f"{int(screen_width)}x{int(screen_height)}")

		# Make the window resizable
		window.resizable(True, True)

		# Let's place the window in the dead center of the screen
		window.geometry(f"{int(screen_width)}x{int(screen_height)}+{int(screen_width / 2)}+{int(screen_height / 2)}")

		# Display the window
		window.mainloop()

	def _handle_keyboard_input(self):
		"""
		This is a while loop that will run in a separate thread to handle keyboard input from the user during the course of the game.
		Potential commands are:
		"quit" - Quit the game
		"restart" - Restart the game
		:return:
		:rtype:
		"""
		while self.running:
			# Get keyboard input from the user
			user_input = input("\nEnter a command: ")

			# Parse the command
			command = user_input.split(" ")[0]

			print("\nYou entered: " + command)

			command = command.upper()

			# Handle the command
			if command == "BORD":
				pass
			elif command == "CREA":
				pass
			elif command == "GAMS":
				pass
			elif command == "GDBY":
				pass
			elif command == "HELO":
				pass
			elif command == "JOIN":
				pass
			elif command == "JOND":
				pass
			elif command == "LIST":
				pass
			elif command == "MOVE":
				pass
			elif command == "QUIT":
				pass
			elif command == "SESS":
				pass
			elif command == "TERM":
				pass
			elif command == "YRMV":
				pass
			else:
				print("Invalid command.")

	def _restart_game(self):
		pass