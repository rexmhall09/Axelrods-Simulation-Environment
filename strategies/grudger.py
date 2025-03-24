def strategy(history):
	if any(opponent_move == "D" for _, opponent_move in history):
			return "D"
	else:
			return "C"
