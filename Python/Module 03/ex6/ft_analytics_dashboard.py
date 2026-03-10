from typing import List, Dict


print("=== Game Analytics Dashboard ===\n")

players: List[str] = ["alice", "bob", "charlie", "diana"]
achievements = set[str](["boss_slayer", "collector", "first_kill", "level_10",
                         "perfectionist", "speed_demon", "treasure_hunter",
                         "level_5", "street_fighter", "magic_master",
                         "elite_smith", "high_scorer"])
regions: set[str] = {"north", "east", "central"}
player_achievements: Dict[str, int] = {"alice": 5, "bob": 3, "charlie": 7}
player_scores: Dict[str, int] = {"alice": 2300, "bob": 1800, "charlie": 2150}
score_categories: Dict[str, int] = {"high": 3, "medium": 2, "low": 1}
total_players: int = len(players)
total_achievements: int = len(achievements)

score: int = 0
player_name: str
for player_name in player_scores:
    score += player_scores[player_name]
total_score: int = sum(player_scores[player_name]
                       for player_name in player_scores)

top_scorer: str = ""
top_score: int = 0
for player_name in player_scores:
    if score > top_score:
        top_score = score
        top_scorer = player_name

high_scorer: List[str] = [player_name for player_name in player_scores if
                          player_scores[player_name] > 2000]
double_scores: List[int] = [player_scores[player_name] * 2
                            for player_name in player_scores]
active_players: List[str] = [player_name for player_name
                             in player_achievements
                             if player_achievements[player_name] >= 3]
average_score: int = total_score / len(active_players)

print("=== List Comprehension Examples ===")
print(f"High scorers (>2000): {high_scorer}")
print(f"Scores doubled: {double_scores}")
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")
print(f"Player scores: {player_scores}")
print(f"Score categories: {score_categories}")
print(f"Achievements counts: {player_achievements}")

print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {players}")
print(f"Unique achievements: {achievements}")
print(f"Active regions: {regions}")

print("\n=== Combined Analysis ===")
print(f"Total players: {total_players}")
print(f"Total unique achievements: {len(achievements)}")
print(f"Average score: {average_score:.2f}")
print(f"Top Performer: {top_scorer} ({player_scores[top_scorer]} points, "
      f"{player_achievements[top_scorer]} achievements)")
