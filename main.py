from enemy.enemy import Enemy
from player.player import Player


class Game:
    # rooms = map_generator()
    print('\n')
    rooms = ['St', 'E', ' ', 'Ex']
    # print(rooms)

    player = Player()
    player.generate_player()
    # print(player.entity.name)

    for r in rooms:
        if r == 'E':
            enemy = Enemy()
            enemy.generate_enemy()
            print(enemy.entity.name)

        elif r == ' ':
            print('Пусто')
        elif r == 'St':
            pass
            # print('Вход')
        elif r == 'Ex':
            pass
            # print('Выход')
