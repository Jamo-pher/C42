from alchemy.grimoire import validate_ingredients, record_spell


def ingredient_spell_validation() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print('validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')

    print('validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print('record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')


def record_spell_late(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import record_spell
    result = record_spell(spell_name, ingredients)
    return (f'record_spell("{spell_name}, "{ingredients}"): {result}')


if __name__ == "__main__":

    ingredient_spell_validation()
    print("\nTesting late import technique:")
    print(record_spell_late("Lightning", "air"))
    print(record_spell_late("Light Barrier", "light"))
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
