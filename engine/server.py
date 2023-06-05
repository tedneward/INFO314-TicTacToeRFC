# This is a server for our Tic-Tac-Toe game. It will communicate over TCP or UDP (user choice) with the client.
"""
Write a TTTP Server (5pts)
create a server that can:
accept requests from mul!ple clients start a game
validate player moves
plays through to game termination
manages up to 10 clients simultaneously
accepts communica!on over TCP or UDP
provides console output about communica!on (diagnostic logging)


MESSAGE PAYLOAD will be:
GAME_ID | SENDER_ID | COMMAND | PAYLOAD

"""


import socket
import time
import datetime
from engine.game import Game
import sys
import threading        # We need this to run multiple games on the server at once
from engine.helpers import prt_dbg
from engine import *
import uuid


class Server:
	def __init__(self, log_level: int=LOGGING, hostname: str=socket.gethostname()):
		"""
		Represents a server for our Tic-Tac-Toe game

		:param log_level: 0 = No logging, 1 = Log to console, 2 = Log to file, 3 = Log to console and file
		:type log_level: int
		"""
		self.id = uuid.uuid4().hex
		self.live_games: list[Game] = []
		self.start = time.time()
		self.start_time = datetime.datetime.now()
		self.running = False
		self.version = 0        # Should be 1 or 2
		self.hostname = hostname
		self.log_level = log_level

		# Socket configurations
		self.tcp_socket = None
		self.udp_socket = None

		self.tcp_clients = set()
		self.tcp_clients_lock = threading.Lock()
		self.tcp_connections = {}
		self.tcp_socket_receive_thread = None
		self.tcp_send_thread = None

		self.udp_clients = set()
		self.udp_clients_lock = threading.Lock()
		self.udp_connections = {}
		self.udp_socket_receive_thread = None
		self.udp_send_thread = None

		self.threads = []

		self._run()

	def __str__(self):
		return f"Server {self.id} running on {self.hostname} started at {self.start_time}"

	def _init_server(self):
		# Initialize the server by creating the sockets, binding them, and setting them on the correct ports

		# TCP
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcp_socket.bind((self.hostname, TCP_PORT))
		self.tcp_socket.listen(MAX_CLIENTS * 2)     # Two players per game and 10 games

		# UDP
		self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.udp_socket.bind((self.hostname, UDP_PORT))
		self.udp_socket_receive_thread = threading.Thread(target=self._udp_receive)
		self.udp_socket_receive_thread.start()

	def _udp_receive(self):
		prt_dbg(f"UDP socket is listening on port {UDP_PORT}.", self.log_level)
		while True:
			data, address = self.udp_socket.recvfrom(1024)
			self._handle_message(data.decode(), "UDP", address)
			prt_dbg(f"Received data from client {address}: {data.decode()} over UDP.", self.log_level)
			# TODO: Handle data here

	def _tcp_receive(self, client, address):
		prt_dbg(f"Accepted connection over TCP from {address}.", self.log_level)
		with self.tcp_clients_lock:
			self.tcp_connections[address] = client
			self.tcp_clients.add(client)
		try:
			while True:
				data = client.recv(1024)
				if not data:
					prt_dbg(f"Client {address} disconnected.", self.log_level)
					break
				prt_dbg(f"Received data from client {address}: {data.decode()} over TCP.", self.log_level)
				with self.tcp_clients_lock:
					self._handle_message(data.decode(), "TCP", address)
		except ConnectionResetError:
			prt_dbg(f"Connection reset by {address}.", self.log_level)
			with self.tcp_clients_lock:
				del self.tcp_connections[address]
				self.tcp_clients.remove(client)
				client.close()
		finally:
			prt_dbg(f"Closing connection with {address}.", self.log_level)
			with self.tcp_clients_lock:
				del self.tcp_connections[address]
				self.tcp_clients.remove(client)
				client.close()


	def _run(self):
		try:
			self._init_server()
			prt_dbg("Now running the server", self.log_level)
			# If we receive a new connection, we will create a new thread to handle it.
			# Also start the thread so it is active.
			while True:
				client, address = self.tcp_socket.accept()
				self.threads.append(threading.Thread(target=self._tcp_receive, args=(client, address)).start())
		except KeyboardInterrupt:
			# Handle a keyboard interrupt by shutting down the server
			prt_dbg("Caught a keyboard interrupt. Server shutting down.", self.log_level)
			self.tcp_socket.close()
			self.udp_socket.close()
			sys.exit()
		except Exception as e:
			prt_dbg(f"Caught an exception: {e}. Server shutting down.", self.log_level)
			self.tcp_socket.close()
			self.udp_socket.close()
			sys.exit()

	def find_games(self) -> list[Game]:
		# Returns a list of joinable games: games that have 1 player and are not in progress
		joinable_games = []
		for game in self.live_games:
			if len(game.players) == 1 and game.game_status == None:
				joinable_games.append(game)
		return joinable_games

	def join_game(self, game_id: str, player_id: str) -> bool:
		# Returns True if the player was successfully joined to the game, False otherwise
		prt_dbg(f"Attempting to add player {player_id} to game {game_id}.", self.log_level)
		for game in self.live_games:
			if game.id == game_id:
				game.add_player_to_game(player_id)
				return True
		prt_dbg(f"failed to add {player_id} to game {game_id} because {game_id} doesn't exist.", self.log_level)
		return False

	def create_game(self, connection_type: str, initial_player_id: str, log_level=LOGGING) -> bool:
		# Creates and adds a game to the self.games list, if possible
		if len(self.live_games) == MAX_CLIENTS - 1:
			raise RuntimeError("Maximum number of games already running. Please try again later.")
		try:
			prt_dbg(f"Creating a new game with player {initial_player_id}.", self.log_level)
			game = Game(connection_type, initial_player_id, log_level)
			self.live_games.append(game)
			return True
		except Exception as e:
			prt_dbg(f"Error creating game: {e}", self.log_level)
			return False

	def _handle_message(self, message: str, socket_type, address = None):
		message_components = message.split("|")
		game_id = message_components[0]
		# Check if a game exists with this ID
		game_exists = False
		for game in self.live_games:
			if game.id == game_id:
				game_exists = True
				break
		if not game_exists:
			if socket_type == "TCP":
				client = self.tcp_connections[address]
				print(client)
				client.sendall("ERROR|Game does not exist.".encode())
			else:
				self.udp_socket.sendto("ERROR|Game does not exist.".encode(), address)
		
		order = message_components[0].upper()
		argument = None

		if len(message_components) == 2:
			sender_id = message_components[1]
		if len(message_components) == 3:
			command = message_components[2]
		if len(message_components) == 4:
			argument = message_components[3]
		
		if order == 'CREA':
			self.create_game(socket_type, address[1])
		# List, Need to change all the prints to send to clients
		elif order == 'LIST':
			for i in range(len(self.live_games)):
				if len(message_components) == 1 and self.live_games[i].game_status == None:
					print(self.live_games[i], 'none')
				elif len(message_components) == 2 and message_components[1] == 'CURR':
					if self.live_games[i].game_status == None or self.live_games[i] == 'IN_PROGRESS':
						print(self.live_games[i], 'curr')
				elif len(message_components) == 2 and message_components[1] == 'ALL':
					print(self.live_games[i], 'all')

		elif order == 'JOIN':
			print(address[1], sender_id)
			if self.join_game(sender_id, address[1]):
				# Successfully joined game
				print(game.board)
			else:
				nip = address[0]
				nad = address[1]
				nad = nad - 1
				naddy = (nip, nad)
				client = self.tcp_connections[naddy]
				client.sendall("error!".encode())
		elif order == 'MOVE':
			if len(message_components) == 1:
				return #error
			
			if(game.players[0] == address[1]):
				tt = 'X'
			else:
				tt = 'O'
			i,j = message_components[1].split(",")
			i = int(i)
			j = int(j)
			
			game.board[2-j][2-i] = tt
			print(game.board) # this needs to be sent back
		elif order == 'QUIT':

			game.game_status = 'Done'

			
