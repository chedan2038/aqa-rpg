import random

from attributes.armor import Armor
from attributes.properties import Properties
from attributes.weapon import Weapon
from base import load_json


class Character:
    def __init__(self):
        self.properties = None
        self.armor = None
        self.weapon = None
        self.character_data_path = None

    def generate_character(self):
        """
        Наделяет персонажа случайными свойствами, броней и оружием.
        """

        data = load_json(self.character_data_path)
        self.properties = Properties(random.choice(list(data['type'])))
        self.armor = Armor(**random.choice(list(data['armor'])))
        self.weapon = Weapon(**random.choice(list(data['weapon'])))
