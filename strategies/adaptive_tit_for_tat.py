import random

def strategy(history):
		if not history:
				return "C"  # Start cooperatively

		# Calculate opponent's cooperation rate
		opponent_moves = [move[1] for move in history]
		cooperation_rate = opponent_moves.count("C") / len(opponent_moves)

		# Randomness element
		if random.random() < 0.05:
				return "D"  # Random defection

		# Check if opponent is largely non-cooperative
		if len(opponent_moves) > 10 and cooperation_rate < 0.3:
				return "D"  # Switch to defecting if opponent defects too often

		# Main Tit for Tat with forgiveness
		last_opponent_move = opponent_moves[-1]
		if last_opponent_move == "D" and cooperation_rate > 0.6:
				return "C"  # Forgive if the overall cooperation is high
		return last_opponent_move  # Otherwise, mirror the opponent
