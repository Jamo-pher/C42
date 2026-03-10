from ex0 import CreatureCard
from ex1 import ArtifactCard, SpellCard, Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    lightning_bolt = SpellCard('Lightning Bolt', 3,
                               'Common', 'Deal 3 damage to target')
    mana_crystal = ArtifactCard('Mana Crystal', 2, 'Common', 1,
                                '+1 mana per turn')
    fire_dragon = CreatureCard("Fire Dragon", 5, 'Rare', 5, 7)

    the_deck = Deck()
    the_deck.add_card(lightning_bolt)
    the_deck.add_card(mana_crystal)
    the_deck.add_card(fire_dragon)

    the_deck.shuffle()
    stats = the_deck.get_deck_stats()

    print("Building deck with different card types...")
    print(f"{stats}")

    print("Drawing and playing cards:\n")

    while True:
        try:
            card = the_deck.draw_card()
            card_type = type(card).__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")
            result = card.play({})
            print(f"Play result: {result}\n")

        except IndexError:
            break

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
