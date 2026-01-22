from base import probability, load_json
from cfg import RED, GREEN, RESET
from enemy.enemy import Enemy
from game_map.game_map import show_position_on_map
from game_map.room import Room
from player.player import Player


class PlayerController:

    def __init__(self, rooms_list: list[Room], player: Player, game_map: list[str], game):
        self.rooms_list = rooms_list
        self.current_room = 0
        self.player = player
        self.game_map = game_map
        self.game = game

    def controller(self) -> None:
        """
         Отображает текущее состояние комнаты, информацию о противнике (если есть) и
         доступные действия игрока, после чего выполняет выбранное действие.
        """

        print('\n')
        show_position_on_map(self.game_map, self.current_room)

        print(f'Перед вами: {self.rooms_list[self.current_room].room_type}')
        if self.rooms_list[self.current_room].enemy:
            print(
                f'Оказалось, что вы здесь не одни: {self.rooms_list[self.current_room].enemy.properties.name}... {self.rooms_list[self.current_room].enemy.properties.description}')
            print(
                f'В его руках: {self.rooms_list[self.current_room].enemy.weapon.description}')
            print(f'На нём: {self.rooms_list[self.current_room].enemy.armor.description}')

        print('\nДоступные действия:')
        available = self._available_actions()
        for k, v in available.items():
            print(f'    {k}. {v[0]}')

        player_action = input()

        if player_action.isdigit() and int(player_action) in available:
            available[int(player_action)][1]()
        else:
            print(f'Нет такого действия, {self.player.properties.name}.\nНа чем мы остановились? Ах, да...\n')

    def _available_actions(self) -> dict:
        """
        Определяет доступные действия на основе окружения.

        :return: Словарь с доступными действиями, где ключ — номер действия, а значение — tuple с названием действия
            и функцией, выполняющей его.
        """

        available_actions = []

        if self.current_room == 0:
            available_actions.append(("Пойти дальше", self._move_forward))
        elif self.current_room == len(self.rooms_list) - 1:
            available_actions.append(("Вернутся назад", self._move_back))
            available_actions.append(("Выйти из подземелья", self._exit_dungeon))
        elif self.rooms_list[self.current_room].enemy:
            available_actions.append(("Вернутся назад", self._move_back))
            available_actions.append(("Атаковать", self._fight))
        elif self.rooms_list[self.current_room].enemy is None:
            available_actions.append(("Пойти дальше", self._move_forward))
            available_actions.append(("Вернутся назад", self._move_back))

        return {k: v for k, v in enumerate(available_actions, 1)}

    def _move_forward(self) -> None:
        """
        Перемещает игрока на одну комнату вперед по карте.
        """

        self.current_room += 1

    def _move_back(self) -> None:
        """
        Перемещает игрока на одну комнату назад по карте.
        """

        self.current_room -= 1

    def _exit_dungeon(self) -> None:
        """
        Выйти и завершить игру.
        """

        print('\nВы покинули это проклятое место. Время перевязать раны и двигаться дальше...')
        self.game.game_status = False

    def _fight(self) -> None:
        """
        Запускает бой между игроком и противником.
        Игрок и враг поочередно наносят удары друг другу, пока здоровье
        одного из них не достигнет 0.
        """

        player = self.player
        enemy = self.rooms_list[self.current_room].enemy

        self._hp_bar(player, fill_color=GREEN,
                     empty_color=GREEN)
        self._hp_bar(enemy, fill_color=RED,
                     empty_color=RED)

        print('Вы решительно бросаетесь на противника! Завязался бой:')

        while enemy.properties.health > 0 and player.properties.health > 0:

            self._attack(
                player,
                enemy,
                f'Вы наносите удар!',
                f'Удар пришелся точно в цель! Вы нанесли',
                f'урона по цели "{enemy.properties.name}".',
                f'Вы не смогли пробить броню "{enemy.armor.name}".',
                f'{enemy.properties.name} смог увернуться от вашего удара.'
            )
            self._hp_bar(enemy, fill_color=RED,
                         empty_color=RED)

            if enemy.properties.health == 0:
                print(
                    f'Вы одержали победу над противником "{enemy.properties.name}"! {enemy.properties.death_description}')
                self.rooms_list[self.current_room].enemy = None
                self.game_map[self.current_room] = load_json('game_map/map_data.json')['entities']['empty']
                break

            self._attack(
                enemy,
                player,
                f'"{enemy.properties.name}" наносит ответный удар. Берегись!',
                f'На этот раз вы не смогли увернуться... "{enemy.properties.name}" нанес вам',
                f'урона.',
                f'Удар был тяжелым, но ваша броня выдержала. Удар не нанес вам урона.',
                f'Удар был внезапным, но вы смогли увернуться. Оружие пролетело в сантиметре от вашего лица.'
            )
            self._hp_bar(player, fill_color=GREEN,
                         empty_color=GREEN)

            if player.properties.health == 0:
                print(f'{player.properties.death_description}')
                self.game.game_status = False
                break

    @staticmethod
    def _attack(
            attacker: Player | Enemy,
            defender: Player | Enemy,
            attack_msg: str,
            hit_msg_1: str,
            hit_msg_2: str,
            fail_msg: str,
            dodge_msg: str
    ) -> None:
        """
        Проводится атака с учетом характеристик снаряжения персонажей.

        :param attacker:
        :param defender:
        :param attack_msg:
        :param hit_msg_1:
        :param hit_msg_2:
        :param fail_msg:
        :param dodge_msg:
        :return:
        """

        print(attack_msg)
        if probability(attacker.weapon.hitting_chance):
            if attacker.weapon.damage > defender.armor.protection:
                damage = attacker.weapon.damage - defender.armor.protection
                defender.properties.health = max(defender.properties.health - damage, 0)
                print(f'{hit_msg_1} "{damage}" {hit_msg_2}')
            elif attacker.weapon.damage < defender.armor.protection:
                print(fail_msg)
        else:
            print(dodge_msg)

    @staticmethod
    def _hp_bar(
            character: Player | Enemy,
            length: int = 20,
            fill_color: str = GREEN,
            empty_color: str = RED
    ) -> None:

        """
        Выводит полоску HP
        :param character:
        :param length:
        :param fill_color:
        :param empty_color:
        """

        ratio = character.properties.health / character.properties.max_health if character.properties.max_health > 0 else 0
        filled = int(length * ratio)
        empty = length - filled
        bar = f'{fill_color}{"█" * filled}{empty_color}{"░" * empty}{RESET}'
        print(
            f'"{character.properties.name}". Здоровье: {character.properties.health}/{character.properties.max_health}\n{bar}')
