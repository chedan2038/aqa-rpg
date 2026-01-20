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

    def fight(self, enemy: Enemy):


        while self.entity.health >= 0 or enemy.entity.health >= 0:

            print('ты', self.entity.health)
            print('враг', enemy.entity.health)

            if probability(self.weapon.hitting_chance):
                print('ты попал')
                if self.weapon.damage > enemy.armor.protection:
                    enemy.entity.health = enemy.entity.health - (self.weapon.damage - enemy.armor.protection)
                elif self.weapon.damage < enemy.armor.protection:
                    print('без урона')
            else:
                print('ты промазал')

            if probability(enemy.weapon.hitting_chance):
                print('враг попал')
                if enemy.weapon.damage > self.armor.protection:
                    self.entity.health = self.entity.health - (enemy.weapon.damage - self.armor.protection)
                elif enemy.weapon.damage < self.armor.protection:
                    print('без урона')
            else:
                print('враг промазал')

            print('ты', self.entity.health)
            print('враг', enemy.entity.health)

# x = Player()
# x.generate_player()
# print(x.__dict__)
#
# print(x.entity.__dict__)
# print(x.armor.__dict__)
# print(x.weapon.__dict__)
