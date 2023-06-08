import sys
import datetime
from engine import LOGGING

def prt_dbg(msg: str, log_level: int=LOGGING):
	"""
	Prints a debug message to the console
	"""
	if log_level > 0:
		sys.stdout.write(f'{datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}: {msg}\n')
