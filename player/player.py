import random

from armor import Armor
from player_data import *
from entity import Entity
from weapon import Weapon


class Player:
    def __init__(self):
        self.entity = None
        self.armor = None
        self.weapon = None

    def generate_player(self):
        self.entity = Entity(player_type)
        self.armor = Armor(random.choice(list(player_armor.values())))
        self.weapon = Weapon(random.choice(list(player_weapon.values())))


# x = Player()
# x.generate_player()
# print(x.__dict__)
#
# print(x.entity.__dict__)
# print(x.armor.__dict__)
# print(x.weapon.__dict__)
