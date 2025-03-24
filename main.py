import os
import importlib.util
import random

# Define a function to import a strategy from a given file path
def import_strategy(path):
		module_name = os.path.splitext(os.path.basename(path))[0]
		spec = importlib.util.spec_from_file_location(module_name, path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		return module.strategy

# Load all strategies from the strategies folder
strategies = {}
strategy_folder = 'strategies'
for filename in os.listdir(strategy_folder):
		if filename.endswith('.py'):
				path = os.path.join(strategy_folder, filename)
				strategy_name = os.path.splitext(filename)[0]
				strategies[strategy_name] = import_strategy(path)

# Define the rules of the Prisoner's Dilemma
def play_round(move1, move2):
		print(move1, move2)
		if move1 == "C" and move2 == "C":
				return (3, 3)
		elif move1 == "C" and move2 == "D":
				return (0, 5)
		elif move1 == "D" and move2 == "C":
				return (5, 0)
		else:
				return (1, 1)

# Simulate a match between two strategies
def play_match(strategy1, strategy2, num_rounds):
		score1, score2 = 0, 0
		history1, history2 = [], []
		for _ in range(num_rounds):
				move1 = strategy1(history2)
				move2 = strategy2(history1)
				history1.append((move1, move2))
				history2.append((move2, move1))
				result = play_round(move1, move2)
				score1 += result[0]
				score2 += result[1]
		# Determine the outcome of the match (win, lose, tie)
		if score1 > score2:
				return score1, score2, 1, 0, 0, 0
		elif score1 < score2:
				return score1, score2, 0, 0, 1, 0
		else:
				return score1, score2, 0, 1, 0, 1

# Run the tournament
results = {name: {"score": 0, "wins": 0, "ties": 0} for name in strategies}
for name1, strategy1 in strategies.items():
		for name2, strategy2 in strategies.items():
				if name1 != name2:
						print("Playing match between", name1, "and", name2, "...")
						score1, score2, win1, tie1, win2, tie2 = play_match(strategy1, strategy2, random.randint(100, 300))
						winner = name1 if score1 > score2 else name2 if score1 < score2 else "TIE"
						print(f"{score1} - {score2} : {winner}\n")
						results[name1]["score"] += score1
						results[name1]["wins"] += win1
						results[name1]["ties"] += tie1
						results[name2]["score"] += score2
						results[name2]["wins"] += win2
						results[name2]["ties"] += tie2

# Calculate final scores with the multiplier
final_scores = {}
for name, result in results.items():
		multiplier = 1 + 1 * result["ties"] + 2 * result["wins"]
		final_scores[name] = result["score"] * multiplier

# Display the results
print("Final Scores:")
for name, final_score in sorted(final_scores.items(), key=lambda item: item[1], reverse=True):
		print(f"{name}: {final_score}")
