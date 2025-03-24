def strategy(history):
		counts = {'C': 0, 'D': 0}
		opponent_history = [move[1] for move in history]
		for move in opponent_history:
				counts[move] += 1
		return 'D' if counts['D'] > counts['C'] else 'C'
		