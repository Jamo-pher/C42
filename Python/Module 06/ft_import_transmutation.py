import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strenght_potion


print("=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

print("\nMethod 2 - Specific funcion import:")
print(f"create_water(): {create_water()}")

print("\nMethod 3 - Aliased import:")
print(f"heal(): {heal()}")

print("\nMethod 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strenght_potion(): {strenght_potion()}")

print("\nAll import transmutation methods mastered!")
