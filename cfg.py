from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_ROOMS_COUNT = 5
DEFAULT_ENEMY_CHANCE = 40
DEFAULT_HP_BAR_LENGTH = 20

EMPTY_ROOM = ' '
ENEMY_ROOM = 'E'
EXIT_ROOM = 'Ex'
START_ROOM = 'St'
ACTION_START_INDEX = 1

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

PLAYER_DATA = 'characters/player/player_data.json'
ENEMY_DATA = 'characters/enemy/enemy_data.json'
