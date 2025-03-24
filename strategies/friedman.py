def strategy(history):
		opponent_history = [move[1] for move in history]
		if 'D' in opponent_history:
				return 'D'
		return 'C'