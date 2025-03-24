def strategy(history):
		probe_sequence = ['D', 'C', 'C']
		opponent_history = [move[1] for move in history]
		if len(opponent_history) < len(probe_sequence):
				return probe_sequence[len(opponent_history)]
		return 'D' if 'C' in opponent_history[:3] else 'C'
		