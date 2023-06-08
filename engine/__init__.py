TCP_PORT = 3116
UDP_PORT = 31161
TIMEOUT = 60 # The number of seconds to wait for a response from the server before timing out
LOGGING = 1 # 0 = No logging, 1 = Log to console
MAX_CLIENTS = 10


SCHEMES = {
	'TCP': 't3tcp://',
	'UDP': 't3udp://',
}



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

CONNECTION_TYPE = {
	"TCP": "TCP",
	"UDP": "UDP"
}