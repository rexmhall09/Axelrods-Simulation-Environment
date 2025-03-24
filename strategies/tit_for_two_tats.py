def strategy(history):
	num_rounds = len(history)
	if num_rounds < 2:
			# Always cooperate if there aren't enough rounds to judge the last two moves
			return 'C'
	# Check the last two moves of the opponent
	last_move = history[-1][1]
	second_last_move = history[-2][1]
	if last_move == 'D' and second_last_move == 'D':
			return 'D'
	return 'C'
	