import random

def strategy(history, defect_probability=0.1):
		if not history:
				return "C"
		else:
				last_opponent_move = history[-1][0]
				if last_opponent_move == "C" and random.random() < defect_probability:
						return "D"
				else:
						return last_opponent_move
