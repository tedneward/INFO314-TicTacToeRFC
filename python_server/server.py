# This is a server for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the client.
import socket
import threading
import random
import sys
import uuid     # For generating unique session IDs
import time
import datetime


class Server:
	def __init__(self):
		self.live_games = []
		self.start_time = datetime.datetime.now()
		self.running = False
		self.hostname = socket.gethostname()
