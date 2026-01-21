import random

from armor import Armor
from base import probability
from enemy.enemy import Enemy
from entity import Entity
from weapon import Weapon
from .player_data import *


class Player:
    def __init__(self):
        self.entity = None
        self.armor = None
        self.weapon = None

    def generate_player(self):
        self.entity = Entity(player_type)
        self.armor = Armor(random.choice(list(player_armor.values())))
        self.weapon = Weapon(random.choice(list(player_weapon.values())))