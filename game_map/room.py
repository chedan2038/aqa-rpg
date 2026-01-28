import random

from base import load_json
from cfg import ENEMY_ROOM
from characters.enemy.enemy import Enemy


class Room:
    def __init__(self, enemy: Enemy | None, room_type: dict):
        self.enemy = enemy
        self.room_type = room_type


def room_generator(game_map: list) -> list[Room]:
    """
    Генерирует комнаты и их окружение исходя из карты.

    :param game_map: Карта подземелья.
    :return: Последовательность комнат.
    """

    rooms = []
    map_data = load_json('game_map/map_data.json')

    for room in game_map:
        if room == ENEMY_ROOM:
            enemy = Enemy()
            enemy.generate_character()
            rooms.append(Room(enemy, random.choice(list(map_data['rooms']))))
        else:
            rooms.append(Room(None, random.choice(list(map_data['rooms']))))

    return rooms
