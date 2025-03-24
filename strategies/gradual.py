def strategy(history):
	if not history:
			return 'C'
	defections = sum(1 for _, move in history if move == 'D')
	count_defections = sum(1 for my_move, _ in history if my_move == 'D')
	if history[-1][1] == 'D':
			return 'D'
	if count_defections < defections:
			return 'D'
	return 'C'