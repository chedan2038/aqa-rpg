from cfg import ENEMY_DATA
from characters.character import Character


class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.character_data_path = ENEMY_DATA
