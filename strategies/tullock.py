def strategy(history):
		opponent_history = [move[1] for move in history]
		rounds_cooperated = len([m for m in opponent_history if m == 'C'])
		defect_rounds = 2 * (len(opponent_history) - rounds_cooperated)
		if defect_rounds > 0:
				return 'D'
		return 'C'
		