import random
import uuid
from datetime import datetime as dt
import sys
from engine import *
from engine.helpers import prt_dbg



class Game:
	def __init__(self, connection_type: GAME_PROTOCOL, initial_player_id: str, log_level=LOGGING):
		"""
		Represents a game of Tic-Tac-Toe
		"""
		if connection_type not in GAME_PROTOCOL:
			raise ValueError(f"Invalid connection type: {connection_type}. Must be one of {GAME_PROTOCOL.keys()} (case-sensitive)")
		self.id = uuid.uuid4().hex
		self._created_at = dt.now()
		if log_level > 0:
			print(f"Creating game {self.id} at {self._created_at}\n")
		self.game_status: GAME_STATUS = None
		self.players: list[str] = [initial_player_id]                # A list of player IDs. The player in index 0 goes first.
		self.protocol = connection_type
		self.log_level = log_level

		self.current_player = None             # Player ID of the player whose turn it is, and we are waiting for

		self.command_queue: list[str] = []

		self.board = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]

	def __str__(self):
		str_to_return = f"Game {self.id}"
		player_count = len(self.players)
		if player_count == 1:
			player_count = " | 1 player (joinable)"
		elif player_count == 2:
			player_count = " | 2 players (in progress)"
		start_time = " | Started at: " + self._created_at.strftime("%m/%d/%Y %H:%M:%S")
		str_to_return = str_to_return + player_count + start_time
		return str_to_return

	def add_player_to_game(self, player_id: str, player_who_should_go_first: str|None=None):
		prt_dbg(f"Adding {player_id} to game {self.id}.", self.log_level)
		# This assumes that there is one other player currently in the game. Raise a ValueError if there is currently not
		if len(self.players) != 1:
			raise ValueError(f"Invalid number of players in game. Expected 1, got {len(self.players)}")
		# self.players.append(player_id)
		# Determine the order of the players
		if player_who_should_go_first is not None:
			if player_who_should_go_first == self.players[0]:
				self.players.append(player_id)
			else:
				self.players.insert(0, player_id)
			self.current_player = self.players[0]
			prt_dbg(f"Player {player_id} has been specified to go first. Setting order to {self.players}", self.log_level)
		else:
			first_player_goes_first = random.random() < 0.5
			if first_player_goes_first:
				self.players.insert(0, player_id)
			else:
				self.players.append(player_id)
			self.current_player = self.players[0]
			prt_dbg(f"Player {player_id} has been randomly selected to go first. Setting order to {self.players}", self.log_level)
		self.game_status = GAME_STATUS['IN_PROGRESS']
