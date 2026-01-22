import pytest

from enemy.enemy import Enemy
from game_map.game_map import map_generator
from game_map.room import room_generator, Room
from player.player import Player
from player_controller import PlayerController


def test_map_generation():
    game_map = map_generator(l=1, e=100)
    assert game_map == ['St', 'E', 'Ex']


@pytest.mark.parametrize('room,enemy', [
    (0, type(None)),
    (1, Enemy),
    (2, type(None)),
    (3, type(None))
])
def test_room_generation(room, enemy):
    rooms = room_generator(['St', 'E', ' ', 'Ex'])
    assert isinstance(rooms[room].enemy, enemy)
    assert isinstance(rooms[room].room_type, str)


def test_player_generation():
    player = Player()
    player.generate_player()

    assert player.properties is not None
    assert player.armor is not None
    assert player.weapon is not None

    assert isinstance(player.properties.health, int)
    assert isinstance(player.armor.name, str)
    assert isinstance(player.weapon.damage, int)


def test_enemy_generation():
    enemy = Enemy()
    enemy.generate_enemy()

    assert enemy.properties is not None
    assert enemy.armor is not None
    assert enemy.weapon is not None

    assert isinstance(enemy.properties.health, int)
    assert isinstance(enemy.armor.name, str)
    assert isinstance(enemy.weapon.damage, int)


def test_player_can_move():
    rooms = [
        Room(None, {}),
        Room(None, {}),
        Room(None, {})
    ]

    controller = PlayerController(rooms, Player(), [''], None)

    assert controller.current_room == 0
    controller._move_forward()
    assert controller.current_room == 1
    controller._move_back()
    assert controller.current_room == 0


@pytest.mark.parametrize('room, expected_action', [
    (1, ['Вернутся назад', 'Атаковать']),
    (2, ['Вернутся назад', 'Выйти из подземелья'])
])
def test_available_actions(room, expected_action):
    rooms = [
        Room(None, {}),
        Room(Enemy(), {}),
        Room(None, {})
    ]
    controller = PlayerController(rooms, Player(), [''], None)
    controller.current_room = room
    actions = controller._available_actions()

    assert list(actions.keys()) == [1, 2]
    assert actions[1][0] == expected_action[0]
    assert actions[2][0] == expected_action[1]


@pytest.mark.parametrize('p_damage, p_hitchance, e_protection, e_expected', [
    (5, 100, 3, 8),
    (5, 100, 5, 10),
    (5, 0, 0, 10)
])
def test_combat(p_damage, p_hitchance, e_protection, e_expected):
    player = Player()
    enemy = Enemy()
    player.generate_player()
    enemy.generate_enemy()

    player.weapon.damage = p_damage
    player.weapon.hitting_chance = p_hitchance

    enemy.properties.max_health = 10
    enemy.properties.health = 10
    enemy.armor.protection = e_protection
    controller = PlayerController([], player, [], None)

    assert enemy.properties.health == 10
    controller._attack(player, enemy, '', '', '', '', '')
    assert enemy.properties.health == e_expected
