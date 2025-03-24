def strategy(history):
	if not history:
			return "C"
	elif len(history) == 1:
			return "D"
	else:
			# Switch to Tit for Tat after the initial test
			last_opponent_move = history[-1][0]
			return last_opponent_move
