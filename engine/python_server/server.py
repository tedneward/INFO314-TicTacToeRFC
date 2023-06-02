# This is a server for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the client.
"""
Write a TTTP Server (5pts)
create a server that can:
accept requests from mul!ple clients start a game
validate player moves
plays through to game termina!on
manages up to 10 clients simultaneously
accepts communica!on over TCP or UDP
provides console output about communica!on (diagnostic logging)
"""

import socket
import time
import datetime
from engine.python_server import *


class Server:
	def __init__(self, log_level: int=LOGGING, max_clients: int=MAX_CLIENTS):
		"""
		Represents a server for our Tic-Tac-Toe game

		:param log_level: 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
		:type log_level: int
		:param max_clients: The maximum number of clients that can connect to the server at once
		:type max_clients: int
		"""
		self.live_games = []
		self.start = time.time()
		self.start_time = datetime.datetime.now()
		self.running = False
		self.version = 0        # Should be 1 or 2
		self.hostname = socket.gethostname()
		self.log_level = log_level
		self.max_clients = max_clients
