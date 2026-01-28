from characters.player.player import Player
from game_map.game_map import map_generator
from game_map.room import room_generator
from player_controller import PlayerController


class Game:

    def __init__(self):
        self.game_status = True

    def run(self):
        print('\n')
        game_map = map_generator()
        rooms = room_generator(game_map)
        player = Player()
        player.generate_character()
        player_controller = PlayerController(rooms, player, game_map, self)

        print(f'Вы: "{player.properties.name}"')
        print(f'В ваших руках: {player.weapon.description}')
        print(f'На вас: {player.armor.description}')

        while self.game_status:
            player_controller.controller()


"""
Плюсы:
- Игра запускается
- Используются отдельные классы для игровых сущностей, отдельный плюс за класс свойств
- Есть параметризация в тестах
- Тесты охватывают основную логику игры

Минусы:
- Нет использования датаклассов
    - Нет общего класса, у enemy/player и weapon/armor, хотя у них есть общие поля.
    - Много последовательных ассертов без описания падений
    - Неинформативные названия переменных, e, row1, k, v и тд
    - Магические значения
    - Не хватает фикстур для тестовых данных
    - Нет использование тернарников (там где это необходимо)
    - Аргументы добавлены в докстринг, но описания нет
    - Тесты не работают из коробки из-за относительных путей к json-файлам
"""

if __name__ == '__main__':
    game = Game()
    game.run()
