import pytest

from characters.enemy.enemy import Enemy
from characters.player.player import Player
from game_map.game_map import map_generator
from game_map.room import Room, room_generator


@pytest.fixture
def player():
    player = Player()
    player.generate_character()
    return player


@pytest.fixture
def enemy():
    enemy = Enemy()
    enemy.generate_character()
    return enemy


@pytest.fixture
def empty_rooms():
    return [
        Room(None, {}),
        Room(None, {}),
        Room(None, {})
    ]


@pytest.fixture
def rooms_with_enemy():
    return [
        Room(None, {}),
        Room(Enemy(), {}),
        Room(None, {})
    ]


@pytest.fixture()
def map_with_enemy():
    return map_generator(length=1, enemy_chance=100)


@pytest.fixture()
def default_room():
    return room_generator(['St', 'E', ' ', 'Ex'])
