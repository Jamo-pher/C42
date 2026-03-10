from typing import Dict, Any
from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
