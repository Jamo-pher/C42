from ex0.CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")

dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
goblin = CreatureCard("Goblin Warrior", 3, "Common", 3, 3)

print("CreatureCard Info:")
print(f"{dragon.get_card_info()}")

print(f"\nPlaying {dragon.name} with 6 mana available")
print(f"Playable: {dragon.is_playable(6)}")

game_state = {'card_played': dragon.name, 'mana': 6, 'battlefield': []}
print(f"Play_result: {dragon.play(game_state)}")

print(f"\n{dragon.name} attacks {goblin.name}:")
print(f"Attack result: {dragon.attack_target(goblin.name)}")

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {dragon.is_playable(3)}")

print("\nAbstract pattern succesfully demonstrated!")
