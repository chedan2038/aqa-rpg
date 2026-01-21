from base import probability
from cfg import RED, GREEN, RESET
from enemy.enemy import Enemy
from game_map.room import Room
from player.player import Player


class PlayerController:

    def __init__(self, rooms_list: list[Room], player: Player, game):
        self.rooms_list = rooms_list
        self.current_room = 0
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
                   ("Атаковать", self._fight), ("Выйти из подземелья", self._exit_dungeon)]
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

    def _fight(self):

        player = self.player
        enemy = self.rooms_list[self.current_room].enemy

        """
        f'"{attacker}" наносит удар'   attack_msg
        print(f'Удар пришелся точно в цель! "{attacker}" нанес "{damage}" единицы урона по "{defender.entity.name}".' hit msg
         f'"{attacker}" не смог пробить {defender.armor.name}'  fail_msg
         f'"{defender.entity.name}" смог уклониться от удара {attacker.entity.name} .' dodge_msg
         f'здоровье {defender.entity.name} {defender.entity.health}' health

        """

        bar = self._hp_bar(player.entity.health, player.entity.max_health, fill_color=GREEN, empty_color=GREEN)
        bar_2 = self._hp_bar(enemy.entity.health, enemy.entity.max_health, fill_color=RED, empty_color=RED)
        print(f'"{player.entity.name}". Здоровье: {player.entity.health}/{player.entity.max_health}\n{bar}')
        print(f'"{enemy.entity.name}". Здоровье: {enemy.entity.health}/{enemy.entity.max_health}\n{bar_2}')

        print('Вы решительно бросаетесь на противника! Завязался бой:')

        while enemy.entity.health > 0 and player.entity.health > 0:

            self._attack(
                player,
                enemy,
                f'Вы наносите удар!',
                f'Удар пришелся точно в цель! Вы нанесли',
                f'урона по цели "{enemy.entity.name}".',
                f'Вы не смогли пробить броню "{enemy.armor.name}".',
                f'{enemy.entity.name} смог увернуться от вашего удара.'
            )

            if enemy.entity.health == 0:
                print(f'Вы одержали победу над противником "{enemy.entity.name}"! {enemy.entity.death_description}')
                self.rooms_list[self.current_room].enemy = None
                break

            self._attack(
                enemy,
                player,
                f'"{enemy.entity.name}" наносит ответный удар. Берегись!',
                f'На этот раз вы не смогли увернуться... "{enemy.entity.name}" нанес вам',
                f'урона.',
                f'Удар был тяжелым, но ваша броня выдержала. Удар не нанес вам урона.',
                f'Удар был внезапным, но вы смогли увернуться. Оружие пролетело в сантиметре от вашего лица.'
            )

            if player.entity.health == 0:
                print(f'{player.entity.death_description}')
                self.game.game_status = False
                break

    def _attack(
            self,
            attacker: Player | Enemy,
            defender: Player | Enemy,
            attack_msg: str,
            hit_msg_1: str,
            hit_msg_2: str,
            fail_msg: str,
            dodge_msg: str
    ):

        print(attack_msg)
        if probability(attacker.weapon.hitting_chance):
            if attacker.weapon.damage > defender.armor.protection:
                damage = attacker.weapon.damage - defender.armor.protection
                defender.entity.health = 0 if defender.entity.health - damage < 0 else defender.entity.health - damage
                print(f'{hit_msg_1} "{damage}" {hit_msg_2}')
            elif attacker.weapon.damage < defender.armor.protection:
                print(fail_msg)
        else:
            print(dodge_msg)

        bar_color = GREEN if isinstance(attacker, Enemy) else RED
        bar = self._hp_bar(defender.entity.health, defender.entity.max_health, fill_color=bar_color,
                           empty_color=bar_color)
        print(f'"{defender.entity.name}". Здоровье: {defender.entity.health}/{defender.entity.max_health}\n{bar}')

    def _hp_bar(
            self,
            current: int,
            maximum: int,
            length: int = 20,
            fill_color: str = GREEN,
            empty_color: str = RED
    ) -> str:
        ratio = current / maximum if maximum > 0 else 0
        filled = int(length * ratio)
        empty = length - filled

        return (
            f'{fill_color}{"█" * filled}'
            f'{empty_color}{"░" * empty}'
            f'{RESET}'
        )
