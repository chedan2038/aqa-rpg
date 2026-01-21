import random


class Entity:
    def __init__(self, entity: dict):
        self.name = self.rand_entity(entity,'name')
        self.health = entity['health']
        self.description = self.rand_entity(entity,'description')
        self.death_description = self.rand_entity(entity,'death_description')
        self.max_health = self.health

    def rand_entity(self, entity: dict, attr: str):
        if isinstance(entity[attr], list):
            return random.choice(entity[attr])
        else:
            return entity[attr]
