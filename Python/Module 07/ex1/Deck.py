from ex0.Card import Card
import random
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")

        card = self.cards[0]
        self.remove_card(card.name)
        return card

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = sum(isinstance(c, CreatureCard) for c in self.cards)
        spells = sum(isinstance(c, SpellCard) for c in self.cards)
        artifacts = sum(isinstance(c, ArtifactCard) for c in self.cards)

        avg_cost = 0.0
        if total > 0:
            avg_cost = sum(c.cost for c in self.cards) / total
            avg_cost = float(f"{avg_cost:.1f}")

        return {'total_cards': total,
                'creatures': creatures,
                'artifacts': artifacts,
                'spells': spells,
                'avg_cots': avg_cost}
