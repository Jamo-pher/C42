from typing import Any, Dict
from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> Dict[str, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        pass
