import json
import random

from cfg import BASE_DIR


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
    :param path: путь
    :return: Данные из json.
    """

    with open(BASE_DIR / path, encoding='utf-8') as file:
        return json.load(file)
