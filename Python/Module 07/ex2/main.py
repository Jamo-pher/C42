from ex2.EliteCard import EliteCard
# from ex0.Card import Card


print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

elite = EliteCard('Arcane Warrior', 5, 'Rare', 5, 3, 7, 4, 'melee')

print(f"Playing {EliteCard.name} (Elite Card):\n")
print("Combat phase:")
print(f"Attack result: {EliteCard.attack}")
