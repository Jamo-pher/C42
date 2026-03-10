from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

    def play(self, game_state: dict) -> Dict[str, Any]:
        self.game_state = game_state
        return {'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target) -> Dict[str, Any]:
        self.target = target
        return {'attacker': self.name,
                'target': self.target,
                'damage_dealt': self.attack,
                'combat_resolved': True}
