class Weapon:
    def __init__(self, weapon: dict):
        self.name = weapon['name']
        self.damage = weapon['damage']
        self.description = weapon['description']
        self.hitting_chance = weapon['hitting_chance']
