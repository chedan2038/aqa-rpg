import random

from armor import Armor
from .enemy_data import *
from entity import Entity
from weapon import Weapon


class Enemy:
    def __init__(self):
        self.entity = None
        self.armor = None
        self.weapon = None

    def generate_enemy(self):
        self.entity = Entity(random.choice(list(enemy_type.values())))
        self.armor = Armor(random.choice(list(enemy_armor.values())))
        self.weapon = Weapon(random.choice(list(enemy_weapon.values())))


# x = Enemy()
# x.generate_enemy()
# print(x.__dict__)
#
# print(x.entity.__dict__)
# print(x.armor.__dict__)
# print(x.weapon.__dict__)
