def strategy(opponent_history):
		if len(opponent_history) > 1 and opponent_history[-1][0] == 'C' and opponent_history[-2][0] == 'C':
				return 'C'
		return 'D'
