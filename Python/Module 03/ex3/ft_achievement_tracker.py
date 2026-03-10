print("=== Achievement Tracker System ===\n")

achievements = set(["boss_slayer", "collector", "first_kill", "level_10",
                    "perfectionist", "speed_demon", "treasure_hunter"])
alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon",
              "perfectionist"])

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {achievements}")
total_unique: int = len(achievements)
print(f"Total unique achievements: {total_unique}\n")

common: str = alice.intersection(bob, charlie)
print(f"Common to all players: {common}")

rare_achievements = set()
for achievement in achievements:
    i = 0
    if achievement in alice:
        i += 1
    if achievement in bob:
        i += 1
    if achievement in charlie:
        i += 1
    if i == 1:
        rare_achievements.add(achievement)
print(f"Rare achievements (1 player): {rare_achievements}")

alice_bob: list = alice.intersection(bob)
alice_unique: list = alice.difference(bob)
bob_unique: list = bob.difference(alice)
print(f"\nAlice vs Bob common: {alice_bob}")
print(f"Alice unique: {alice_unique}")
print(f"Bob unique: {bob_unique}")
