import random

from attributes.armor import Armor
from attributes.properties import Properties
from attributes.weapon import Weapon
from base import load_json


class Enemy:
    def __init__(self):
        self.properties = None
        self.armor = None
        self.weapon = None

    def generate_enemy(self):
        """
         Наделяет вражину случайными свойствами, броней и оружием.
         (Не путать с игроком - это другое..)
        """

        enemy_data = load_json('enemy/enemy_data.json')
        self.properties = Properties(random.choice(list(enemy_data['type'])))
        self.armor = Armor(random.choice(list(enemy_data['armor'])))
        self.weapon = Weapon(random.choice(list(enemy_data['weapon'])))
