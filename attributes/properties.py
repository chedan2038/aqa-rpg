import random
from typing import Any


class Properties:
    def __init__(self, entity: dict):
        self.name = self.rand_properties(entity, 'name')
        self.health = entity['health']
        self.description = self.rand_properties(entity, 'description')
        self.death_description = self.rand_properties(entity, 'death_description')
        self.max_health = self.health

    @staticmethod
    def rand_properties(properties: dict, attr: str) -> Any:
        """
        Если значение по ключу attr является списком, выбирается случайный элемент.
        Иначе возвращается само значение.

        :param properties: Словарь свойств персонажа
        :param attr: Ключ
        :return: Случайное значение свойства из словаря характеристик.
        """

        return random.choice(properties[attr]) if isinstance(properties[attr], list) else properties[attr]
