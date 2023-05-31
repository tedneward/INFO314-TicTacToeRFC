import random
import uuid


## Define "Types" for the game
GAME_PROTOCOL = {
	"TCP": 0,
	"UDP": 0
}

GAME_STATUS = {
	"NOT_STARTED": 0,
	"SEEKING_ADDITIONAL_PLAYER": 1,
	"IN_PROGRESS": 2,
	"COMPLETE": 3
}


class Game:
	def __init__(self):
		"""
		Represents a game of Tic-Tac-Toe
		"""
		self._id = uuid.uuid4().hex
		self.game_status: GAME_STATUS = None
		self.name: str|None = None
		self.players: list[str] = []                # A list of player IDs. The player in index 0 is the host.
		self.moving_first = None					# The player ID of the player who is moving first
		self.protocol: GAME_PROTOCOL = None         # Either "TCP" or "UDP"

		self.command_queue: list[str] = []

		self.board = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]