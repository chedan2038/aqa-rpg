import pytest

from characters.enemy.enemy import Enemy
from characters.player.player import Player
from game_map.room import room_generator
from player_controller import PlayerController


def test_map_generation(map_with_enemy):
    assert map_with_enemy == ['St', 'E', 'Ex'], 'Не совпадает карта'


@pytest.mark.parametrize('room,enemy', [
    (0, type(None)),
    (1, Enemy),
    (2, type(None)),
    (3, type(None))
])
def test_room_generation(room, enemy, default_room):
    rooms = room_generator(['St', 'E', ' ', 'Ex'])
    assert isinstance(rooms[room].enemy,
                      enemy), f'Не совпадение карты и текущей комнаты: карта:{rooms[room]} противник:{enemy}'
    assert isinstance(rooms[room].room_type, str), 'Отсутствует описание комнаты'


def test_player_generation(player):
    assert player.properties is not None, 'У игрока нет свойств (здоровье, описание, имя и тд)'
    assert player.armor is not None, 'У игрока нет брони'
    assert player.weapon is not None, 'У игрока нет оружия'


def test_enemy_generation(enemy):
    assert enemy.properties is not None, 'У противника нет свойств (здоровье, описание, имя и тд)'
    assert enemy.armor is not None, 'У противника нет брони'
    assert enemy.weapon is not None, 'У противника нет оружия'


def test_player_can_move(empty_rooms, player):
    controller = PlayerController(empty_rooms, player, [''], None)

    assert controller.current_room == 0, 'Позиция стартовой комнаты неверна'
    controller._move_forward()
    assert controller.current_room == 1, 'Ожидаемая позиция комнаты не совпадает'
    controller._move_back()
    assert controller.current_room == 0, 'Ожидаемая позиция комнаты не совпадает'


@pytest.mark.parametrize('room, expected_action', [
    (1, ['Вернутся назад', 'Атаковать']),
    (2, ['Вернутся назад', 'Выйти из подземелья'])
])
def test_available_actions(room, expected_action, rooms_with_enemy):
    controller = PlayerController(rooms_with_enemy, Player(), [''], None)
    controller.current_room = room
    actions = controller._available_actions()

    assert list(actions.keys()) == [1, 2], 'Не совпадают ожидаемый и доступные действия'
    assert actions[1][0] == expected_action[0], 'Не совпадают ожидаемый и доступные действия'
    assert actions[2][0] == expected_action[1], 'Не совпадают ожидаемый и доступные действия'


@pytest.mark.parametrize('p_damage, p_hitchance, e_protection, e_expected', [
    (5, 100, 3, 8),
    (5, 100, 5, 10),
    (5, 0, 0, 10)
])
def test_combat(p_damage, p_hitchance, e_protection, e_expected, player, enemy):
    player.weapon.damage = p_damage
    player.weapon.hitting_chance = p_hitchance

    enemy.properties.max_health = 10
    enemy.properties.health = 10
    enemy.armor.protection = e_protection
    controller = PlayerController([], player, [], None)

    controller._attack(player, enemy, '', '', '', '', '')
    assert enemy.properties.health == e_expected, 'Неверный расчет урона'
