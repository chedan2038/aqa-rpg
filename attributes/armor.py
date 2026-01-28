from dataclasses import dataclass

from attributes.item import Item


@dataclass
class Armor(Item):
    protection: int
