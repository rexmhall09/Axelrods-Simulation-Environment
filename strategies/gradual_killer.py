def strategy(history):
		opponent_history = [move[1] for move in history]
		defection_count = opponent_history.count('D')
		if defection_count > 0:
				return 'D'
		return 'C'
		