def strategy(history):
		opponent_history = [move[1] for move in history]
		if len(opponent_history) < 3:
				return 'C'
		cooperation_rate = opponent_history.count('C') / len(opponent_history)
		return 'C' if cooperation_rate > 0.5 else 'D'
	