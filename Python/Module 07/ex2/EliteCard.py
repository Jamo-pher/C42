from typing import Any, Dict
from ex0.Card import Card
from ex2 import Combatable, Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 defense: int, spell_power: int, mana: int,
                 combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense = defense
        self.mana = mana
        self.combat_type = combat_type
        self.spell_power = spell_power

    def play(self, game_state: dict) -> Dict[str, Any]:
        return game_state

    def attack(self, target) -> dict:
        return {'attacker': self.name, 'target': target,
                'damage': self.attack_power,
                'combat_type': self.combat_type}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        self.incoming_damage = incoming_damage
        damage_blocked: int = 0
        if self.defense >= self.incoming_damage:
            self.damage_taken = 0
        else:
            self.damage_taken = self.incoming_damage - self.defense
        if self.defense >= self.incoming_damage:
            damage_blocked = self.incoming_damage
        else:
            damage_blocked = self.defense
        self.damage_taken = self.incoming_damage - self.defense
        return {'defender': self.name, 'damage_taken': self.damage_taken,
                'damage_blocked': damage_blocked, 'still_alive': True}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {'caster': self.name, 'spell': spell_name, 'targets': [targets],
                'mana_used': self.mana}

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> Dict[str, Any]:
        stats = {'mana': self.mana, 'spell_power': self.spell_power}
        return stats
