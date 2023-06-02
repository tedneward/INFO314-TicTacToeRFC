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
from game import Game
import sys


# Define constants
TCP_PORT = 3116
UDP_PORT = 31161
TIMEOUT = 60 # The number of seconds to wait for a response from the server before timing out
LOGGING = 1 # 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
MAX_CLIENTS = 10

class Server:
	def __init__(self, log_level: int=LOGGING):
		"""
		Represents a server for our Tic-Tac-Toe game

		:param log_level: 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
		:type log_level: int
		"""
		self.live_games: list[Game] = []
		self.start = time.time()
		self.start_time = datetime.datetime.now()
		self.running = False
		self.version = 0        # Should be 1 or 2
		self.hostname = socket.gethostname()
		self.log_level = log_level
		self.max_clients = MAX_CLIENTS      # Default is 10, as defined in the RFC

	def find_games(self) -> list[Game]:
		# Returns a list of joinable games: games that have 1 player and are not in progress
		joinable_games = []
		for game in self.live_games:
			if len(game.players) == 1 and game.game_status == 0:
				joinable_games.append(game)
		return joinable_games

	def join_game(self, game_id: str, player_id: str) -> bool:
		# Returns True if the player was successfully joined to the game, False otherwise
		if self.log_level > 0:
			sys.stdout.write(f"Attempting to add player {player_id} to game {game_id}.\n")
		for game in self.live_games:
			if game.id == game_id:
				game.add_player_to_game(player_id)
				return True
		return False
