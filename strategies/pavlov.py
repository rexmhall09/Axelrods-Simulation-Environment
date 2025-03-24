def strategy(history):
	if not history or len(history) == 1:
			return 'C'  # Start with cooperation
	last_round = history[-1]
	my_last_move, opponent_last_move = last_round
	if my_last_move == opponent_last_move:
			return my_last_move  # Stay if won the last round
	else:
			return 'D' if my_last_move == 'C' else 'C'  # Shift if lost the last round
