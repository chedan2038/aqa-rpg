from base import probability
from cfg import RED, GREEN, RESET
from enemy.enemy import Enemy
from game_map.game_map import show_position_on_map
from game_map.map_data import map_ents
from game_map.room import Room
from player.player import Player


class PlayerController:

    def __init__(self, rooms_list: list[Room], player: Player, game_map: list[str], game):
        self.rooms_list = rooms_list
        self.current_room = 0
        self.player = player
        self.game_map = game_map
        self.game = game

    def controller(self):
        """Доступные действия:
                    1. Пойти дальше
                    2. Вернутся назад
                    3. Атаковать
                    4. Выйти из подземелья"""

        print('\n')
        show_position_on_map(self.game_map, self.current_room)

        print(f'Перед вами: {self.rooms_list[self.current_room].room_type}')
        if self.rooms_list[self.current_room].enemy is not None:
            print(
                f'Оказалось, что вы здесь не одни: {self.rooms_list[self.current_room].enemy.entity.name}... {self.rooms_list[self.current_room].enemy.entity.description}')
            print(
                f'В его руках: {self.rooms_list[self.current_room].enemy.weapon.description}')
            print(f'На нём: {self.rooms_list[self.current_room].enemy.armor.description}')

        print('Доступные действия:')
        available = self._available_actions()
        for k, v in available.items():
            print(f'    {k}. {v[0]}')

        player_action = input()

        if player_action.isdigit() and int(player_action) in available:
            available[int(player_action)][1]()
        else:
            print(f'Нет такого действия, {self.player.entity.name}.\nНа чем мы остановились? Ах, да...\n')

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
        print('\nВы покинули это проклятое место. Время перевязать раны и двигаться дальше...')
        self.game.game_status = False

    def _fight(self):

        player = self.player
        enemy = self.rooms_list[self.current_room].enemy

        self._hp_bar(player, fill_color=GREEN,
                     empty_color=GREEN)
        self._hp_bar(enemy, fill_color=RED,
                     empty_color=RED)

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
                self.game_map[self.current_room] = map_ents['empty']
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
                defender.entity.health = max(defender.entity.health - damage, 0)
                print(f'{hit_msg_1} "{damage}" {hit_msg_2}')
            elif attacker.weapon.damage < defender.armor.protection:
                print(fail_msg)
        else:
            print(dodge_msg)

        bar_color = GREEN if isinstance(attacker, Enemy) else RED
        self._hp_bar(defender,fill_color=bar_color,
                           empty_color=bar_color)


    def _hp_bar(
            self,
            character: Player | Enemy,
            length: int = 20,
            fill_color: str = GREEN,
            empty_color: str = RED
    ) -> None:
        ratio = character.entity.health / character.entity.max_health if character.entity.max_health > 0 else 0
        filled = int(length * ratio)
        empty = length - filled

        bar = f'{fill_color}{"█" * filled}{empty_color}{"░" * empty}{RESET}'
        print(f'"{character.entity.name}". Здоровье: {character.entity.health}/{character.entity.max_health}\n{bar}')



