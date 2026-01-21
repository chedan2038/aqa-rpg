from base import probability
from game_map.room import Room
from player.player import Player


class PlayerController:

    def __init__(self, rooms_list: list[Room], player: Player, game):
        self.rooms_list = rooms_list
        self.current_room = 2
        self.player = player
        self.game = game

    def controller(self):
        """Доступные действия:
                    1. Пойти дальше
                    2. Вернутся назад
                    3. Атаковать
                    4. Выйти из подземелья"""

        print('Доступные действия:')
        available = self._available_actions()
        for k, v in available.items():
            print(f'    {k}. {v[0]}')

        player_action = int(input())

        if player_action in available:
            available[player_action][1]()
        else:
            print('Нет такого действия, сынок')

    def _available_actions(self):
        actions = [("Пойти дальше", self._move_forward), ("Вернутся назад", self._move_back),
                   ("Атаковать", self._attack), ("Выйти из подземелья", self._exit_dungeon)]
        # убрать

        available_actions = []

        if self.current_room == 0:
            available_actions.append(actions[0])
        elif self.current_room == len(self.rooms_list) - 1:
            available_actions.append(actions[1])
            available_actions.append(actions[3])
        elif self.rooms_list[self.current_room].enemy:
            available_actions.append(actions[1])
            available_actions.append(actions[2])
        elif self.rooms_list[self.current_room].enemy is None:
            available_actions.append(actions[0])
            available_actions.append(actions[1])

        return {k: v for k, v in enumerate(available_actions, 1)}

    def _move_forward(self):
        self.current_room += 1

    def _move_back(self):
        self.current_room -= 1

    def _exit_dungeon(self):
        print('выход')
        self.game.game_status = False

    def _attack(self):
        # пофиксить дублирование

        while self.player.entity.health >= 0 and self.rooms_list[self.current_room].enemy.entity.health >= 0:

            print('p', self.player.entity.health, 'e', self.rooms_list[self.current_room].enemy.entity.health)

            if probability(self.player.weapon.hitting_chance):
                # print('ты попал')
                if self.player.weapon.damage > self.rooms_list[self.current_room].enemy.armor.protection:
                    self.rooms_list[self.current_room].enemy.entity.health = self.rooms_list[
                                                                                 self.current_room].enemy.entity.health - (
                                                                                         self.player.weapon.damage -
                                                                                         self.rooms_list[
                                                                                             self.current_room].enemy.armor.protection)
                elif self.player.weapon.damage < self.rooms_list[self.current_room].enemy.armor.protection:
                    print('без урона')
            else:
                print('ты промазал')

            if probability(self.rooms_list[self.current_room].enemy.weapon.hitting_chance):
                # print('враг попал')
                if self.rooms_list[self.current_room].enemy.weapon.damage > self.player.armor.protection:
                    self.player.entity.health = self.player.entity.health - (
                                self.rooms_list[self.current_room].enemy.weapon.damage - self.player.armor.protection)
                elif self.rooms_list[self.current_room].enemy.weapon.damage < self.player.armor.protection:
                    print('без урона')
            else:
                print('враг промазал')

        if self.player.entity.health > self.rooms_list[self.current_room].enemy.entity.health:
            print('Ты победил')
        else:
            print('Ты проиграл')
