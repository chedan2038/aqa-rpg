from base import probability
from .map_data import map_ents, map_base


def map_generator(l=10, ep=60) -> list:
    """
    :param l: кол-во комнат без учета входа и выхода
    :param ep: вероятность появления противника
    :return:
    """

    current_map = [*map_base.keys()]
    enemy, empty = map_ents.keys()

    for i in range(l):
        if probability(ep):
            current_map.insert(-1, enemy)
        else:
            current_map.insert(-1, empty)

    return current_map

