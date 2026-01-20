import random

from enemy.enemy import Enemy
from game_map.map_data import map_ents, rooms_type




class Room:
    def __init__(self, enemy: Enemy | None, room_type: dict):
        self.enemy = enemy
        self.room_type = room_type

def room_generator(game_map: list)-> list[Room]:
    rooms = []

    for r in game_map:
        if r == map_ents['enemy']:
            enemy = Enemy()
            enemy.generate_enemy()
            rooms.append(Room(enemy, random.choice(list(rooms_type.values()))))
        else:
            rooms.append(Room(None, random.choice(list(rooms_type.values()))))

    return rooms