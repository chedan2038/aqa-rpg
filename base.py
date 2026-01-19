import random


def probability(p: int) -> bool:
    """
    Вероятность срабатывания предмета/действия
    :param p: число от 0 до 100
    :return bool
    """
    p = p / 100
    return random.random() < p
