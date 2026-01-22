import json
import random


def probability(p: int) -> bool:
    """
    Вероятность срабатывания предмета/действия
    :param p: число от 0 до 100
    :return bool
    """
    p = p / 100
    return random.random() < p


def load_json(path: str) -> dict:
    with open(path, encoding='utf-8') as file:
        return json.load(file)
