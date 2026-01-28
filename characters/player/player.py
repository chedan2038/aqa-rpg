from cfg import PLAYER_DATA
from characters.character import Character


class Player(Character):
    def __init__(self):
        super().__init__()
        self.character_data_path = PLAYER_DATA
