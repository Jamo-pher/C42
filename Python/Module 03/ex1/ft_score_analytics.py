import sys
from typing import List

print("=== Player Score Analytics ===")
args: List[str] = sys.argv[1:]
if (len(sys.argv) < 2):
    print("No scores provided. Usage: python3 ft_score_analytics.py "
          "<score1> <score2> ...")
else:
    scores: List[int] = []
    arg: str
    try:
        for arg in args:
            scores.append(int(arg))
    except ValueError:
        print("Error: Argument must be a number")

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: int = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"Hight score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")
