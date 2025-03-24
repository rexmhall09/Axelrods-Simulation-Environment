def strategy(history):
	num_rounds = len(history)
	if history == []:
			# Always defect if there aren't enough rounds to judge the last two moves
			return 'D'
	elif num_rounds == 1:
			#do what the opponent did last round
			return history[0][0]
	elif num_rounds < 99:
			num_rounds = len(history)
			# Check the last two moves of the opponent
			last_move = history[-1][1]
			second_last_move = history[-2][1]
			if last_move == 'D' and second_last_move == 'D':
					return 'D'
			return 'C'
	elif num_rounds == 99:
			# Check if currently losing and decide whether to extend Tit for Tat
			my_score = 0
			opponent_score = 0
			for my_move, opponent_move in history:
					if my_move == 'C' and opponent_move == 'C':
							my_score += 3
							opponent_score += 3
					elif my_move == 'C' and opponent_move == 'D':
							my_score += 0
							opponent_score += 5
					elif my_move == 'D' and opponent_move == 'C':
							my_score += 5
							opponent_score += 0
					elif my_move == 'D' and opponent_move == 'D':
							my_score += 1
							opponent_score += 1
			# Extend Tit for Tat by one more round if losing
			if my_score < opponent_score:
					return history[-1][1]
	# Default to always defect after the initial period
	return 'D'
