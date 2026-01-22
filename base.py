import json
import random


def probability(p: int) -> bool:
    """
    Определяет, сработает ли действие с заданной вероятностью.

    :param p: Вероятность срабатывания в процентах (0–100)
    :return bool
    """

    p = p / 100
    return random.random() < p


def load_json(path: str) -> dict:
    """
    :param path:
    :return: Данные из json.
    """

    with open(path, encoding='utf-8') as file:
        return json.load(file)
