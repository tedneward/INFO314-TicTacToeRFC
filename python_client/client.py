# This is a Client for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the server.
from tkinter import *
import socket

class Client:
	def __init__(self):
		self.running = False
		self.window_title = "Tic-Tac-Toe Client"

		# Start the client
		self._start()

	def _start(self):
		"""
		Set up the window and start the client
		"""
		# Create the main window
		window = Tk(screenName=self.window_title)
		window.title(self.window_title)

		# Create a label
		window_title_label = Label(window, text="Tic-Tac-Toe Client")

		# Place the label where there is space
		window_title_label.pack()

		# Create a start-game button
		start_game_button = Button(window, text="Start Game")

		# Create a restart-game button
		restart_game_button = Button(window, text="Restart Game")

		# Create an "Enter Game Code" label
		enter_game_code_label = Label(window, text="Enter Game Code")

		# Create a text-entry field for the game code
		game_code_entry = Entry(window)


		# Display the window
		window.mainloop()
