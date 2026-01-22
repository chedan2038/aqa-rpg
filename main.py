from game_map.game_map import map_generator
from game_map.room import room_generator
from player.player import Player
from player_controller import PlayerController


class Game:

    def __init__(self):
        self.game_status = True

    def run(self):
        print('\n')
        game_map = map_generator()
        rooms = room_generator(game_map)
        player = Player()
        player.generate_player()
        player_controller = PlayerController(rooms, player, game_map, self)

        print(f'Вы: "{player.properties.name}"')
        print(f'В ваших руках: "{player.weapon.description}"')
        print(f'На вас: "{player.armor.description}"')

        while self.game_status:
            player_controller.controller()


if __name__ == '__main__':
    game = Game()
    game.run()
