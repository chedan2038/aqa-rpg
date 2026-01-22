import random

from attributes.armor import Armor
from attributes.properties import Properties
from attributes.weapon import Weapon
from base import load_json


class Player:
    def __init__(self):
        self.properties = None
        self.armor = None
        self.weapon = None

    def generate_player(self) -> None:
        """
        Наделяет игрока случайными свойствами, броней и оружием.
        """

        player_data = load_json('player/player_data.json')
        self.properties = Properties(random.choice(list(player_data['type'])))
        self.armor = Armor(random.choice(list(player_data['armor'])))
        self.weapon = Weapon(random.choice(list(player_data['weapon'])))
