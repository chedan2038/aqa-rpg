import random

from armor import Armor
from base import probability, load_json
from enemy.enemy import Enemy
from entity import Entity
from weapon import Weapon



class Player:
    def __init__(self):
        self.entity = None
        self.armor = None
        self.weapon = None

    def generate_player(self):
        player_data = load_json('player/player_data.json')
        self.entity = Entity(random.choice(list(player_data['type'])))
        self.armor = Armor(random.choice(list(player_data['armor'])))
        self.weapon = Weapon(random.choice(list(player_data['weapon'])))

