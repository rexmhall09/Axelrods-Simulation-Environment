def strategy(history):
	if not history:
			return 'D'
	last_round = history[-1]
	opponent_last_move = last_round[1]
	return opponent_last_move