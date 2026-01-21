from base import probability
from cfg import RED,GREEN,RESET
from .map_data import map_ents, map_base


def map_generator(l=10, ep=40) -> list:
    """
    :param l: кол-во комнат без учета входа и выхода
    :param ep: вероятность появления противника
    :return:
    """

    current_map = [*map_base.values()]

    for i in range(l):
        if probability(ep):
            current_map.insert(-1, map_ents['enemy'])
        else:
            current_map.insert(-1, map_ents['empty'])

    return current_map




def show_position_on_map(game_map: list[str], current_room:int):

    row1 = ''
    for tile in game_map:
        if tile == 'E':
            row1 += f'[{RED}{tile}{RESET}]  '
        else:
            row1 += f'[{tile}]  '
    print(row1.rstrip())

    pointer_row = ''
    for idx, tile in enumerate(game_map):
        length = len(f'[{tile}]')
        if idx == current_room:
            pointer_row += ' ' * (length // 2) + f'{GREEN}^{RESET}' + ' ' * (length - length // 2)
        else:
            pointer_row += ' ' * length
        pointer_row += '  '

    print(pointer_row.rstrip())