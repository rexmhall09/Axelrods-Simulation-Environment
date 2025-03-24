def strategy(opponent_history):
		if not opponent_history:
				return 'C'
		if len(opponent_history) < 3:
				return 'C'
		if opponent_history[-1][0] == 'D' and opponent_history[-2][0] == 'D':
				return 'D'
		return 'C'
