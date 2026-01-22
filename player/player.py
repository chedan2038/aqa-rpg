import random

from armor import Armor
from base import probability, load_json
from enemy.enemy import Enemy
from properties import Properties
from weapon import Weapon



class Player:
    def __init__(self):
        self.properties = None
        self.armor = None
        self.weapon = None

    def generate_player(self):
        player_data = load_json('player/player_data.json')
        self.properties = Properties(random.choice(list(player_data['type'])))
        self.armor = Armor(random.choice(list(player_data['armor'])))
        self.weapon = Weapon(random.choice(list(player_data['weapon'])))

