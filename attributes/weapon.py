from dataclasses import dataclass

from attributes.item import Item


@dataclass
class Weapon(Item):
    damage: int
    hitting_chance: int
