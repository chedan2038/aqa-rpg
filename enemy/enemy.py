import random

from armor import Armor
from base import load_json
from properties import Properties
from weapon import Weapon


class Enemy:
    def __init__(self):
        self.properties = None
        self.armor = None
        self.weapon = None

    def generate_enemy(self):
        enemy_data = load_json('enemy/enemy_data.json')
        self.properties = Properties(random.choice(list(enemy_data['type'])))
        self.armor = Armor(random.choice(list(enemy_data['armor'])))
        self.weapon = Weapon(random.choice(list(enemy_data['weapon'])))

