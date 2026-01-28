from base import probability
from cfg import RED, GREEN, RESET, DEFAULT_ROOMS_COUNT, DEFAULT_ENEMY_CHANCE, START_ROOM, EXIT_ROOM, ENEMY_ROOM, \
    EMPTY_ROOM


def map_generator(length: int = DEFAULT_ROOMS_COUNT, enemy_chance: int = DEFAULT_ENEMY_CHANCE) -> list:
    """
    Генерирует карту подземелья.

    :param length: Кол-во комнат без учета входа и выхода.
    :param enemy_chance: Вероятность появления противника.
    :return: Последовательность комнат.
    """

    current_map = [START_ROOM, EXIT_ROOM]

    for room_count in range(length):
        if probability(enemy_chance):
            current_map.insert(-1, ENEMY_ROOM)
        else:
            current_map.insert(-1, EMPTY_ROOM)

    return current_map


def show_position_on_map(game_map: list[str], current_room: int) -> None:
    """
    Показывает текущее местоположение персонажа на карте.

    :param game_map: Карта подземелья.
    :param current_room: Текущая комната
    """

    row = ''
    for tile in game_map:
        if tile == ENEMY_ROOM:
            row += f'[{RED}{tile}{RESET}]  '
        else:
            row += f'[{tile}]  '
    print(row.rstrip())

    pointer_row = ''
    for idx, tile in enumerate(game_map):
        length = len(f'[{tile}]')
        if idx == current_room:
            pointer_row += ' ' * (length // 2) + f'{GREEN}^{RESET}' + ' ' * (length - length // 2)
        else:
            pointer_row += ' ' * length
        pointer_row += '  '

    print(pointer_row.rstrip())
