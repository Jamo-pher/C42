from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability must be a positive integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        self.game_state = game_state
        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': f'Permanent: {self.effect}'}

    def activate_skill(self) -> Dict[str, Any]:
        if self.durability >= 0:
            self.durability -= 1
            return {'artifact': self.name,
                    'durability': self.durability,
                    'effect': self.effect,
                    'activated': True}
        else:
            return {'artifact': self.name,
                    'activated': False,
                    'reason': 'Artifact is broken and cannot be activated'}

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["durability"] = self.durability
        info["effect"] = self.effect
        info["type"] = "Artifact"
        return info
