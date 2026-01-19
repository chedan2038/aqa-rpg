from base import probability

map_ents = {
    "E": "враг",
    " ": "пустая комната"
}

map_base = {
    "St": "стартовая точка",
    "Ex": "выход из подземелья"
}


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



