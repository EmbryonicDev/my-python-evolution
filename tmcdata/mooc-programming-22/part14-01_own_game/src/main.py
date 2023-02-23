import pygame
import random
from Timer import Timer
from ScreenObjects import ScreenObject, MovingObject, MovingMonster, MovingCoin, BonusCoin, Robot


class GetCoin:
    def __init__(self):
        pygame.init()

        # Window
        self.width = 1000
        self.height = 900
        self.info_board = 100
        self.bonus_board = 100
        self.luck_board = 80
        self.total_height = self.height+self.info_board+self.bonus_board+self.luck_board
        self.window_dimensions = (self.width, self.height)
        self.window = pygame.display.set_mode(
            (self.width, self.total_height))
        pygame.display.set_caption('Coin Chaser')

        self.game_font = pygame.font.SysFont('Arial', 36)
        self.heading_font = pygame.font.SysFont('Arial', 72)
        self.door = ScreenObject(self.window_dimensions, 'door')
        self.clock = pygame.time.Clock()
        self.new_game()
        self.main_loop()

    def new_game(self):
        self.timer = Timer()
        self.random_color = (random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        self.game_over = False
        self.game_paused = False
        self.level = 1
        self.monster_count = 1
        self.monsters = []
        self.bonus_record = {'freeze': 0, 'speed up': 0, 'cupcake': 0,
                             'add monsters': 0, 'add health': 0, 'take health': 0}
        self.luck_count = {'good': 0, 'bad': 0, 'total count': 0,
                           'good percentage': 0, 'bad percentage': 0}
        self.bonus_coin = self.get_bonus_coin()
        self.bot = Robot(self.window_dimensions, 'robot')
        self.release_coins()
        self.release_monsters()

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            if not self.game_over and not self.game_paused:
                self.timer.add_counter()
                self.move_coin()
                self.move_bonus_coin()
                self.move_bot()
                self.move_monster()

    def check_events(self):
        key_dict = {
            pygame.K_LEFT: self.bot.toggle_left,
            pygame.K_RIGHT:  self.bot.toggle_right,
            pygame.K_UP:  self.bot.toggle_up,
            pygame.K_DOWN:  self.bot.toggle_down,
            pygame.K_F2:  self.new_game,
            pygame.K_SPACE:  self.toggle_game_over,
            pygame.K_ESCAPE:  exit
        }

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in key_dict:
                    key_dict[event.key]()

            if event.type == pygame.KEYUP:
                if (event.key in key_dict and
                        event.key != pygame.K_SPACE):
                    key_dict[event.key]()

            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        dark_grey = (64, 64, 64)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)
        orange = (255, 153, 51)

        # helper functions
        # standard text render
        def get_plain_text(font, text, color):
            return font.render(text, True, color)

        # text render with variable
        def get_text_with_variable(font, text, variable, color: tuple):
            return font.render(
                f"{text}: {variable}", True, color)

        def handle_window_text():
            # get game over text
            if self.game_over:
                game_text = get_plain_text(
                    self.heading_font, 'Game Over...', white)
            # get game paused text
            if self.game_paused:
                game_text = get_plain_text(
                    self.heading_font, 'Game Paused...', white)

            if self.game_paused or self.game_over:
                # text background
                pygame.draw.rect(self.window, dark_grey,
                                 (self.width/2-game_text.get_width() / 2-8, self.height/2 -
                                  game_text.get_height()/2-8, game_text.get_width()+8, game_text.get_height()+8))
                # text
                self.window.blit(game_text, (self.width/2-game_text.get_width() /
                                             2, self.height/2-game_text.get_height()/2))

        def get_dividing_lines():
            # 1st dividing line
            pygame.draw.line(self.window, yellow,
                             (0, self.height), (self.width, self.height), 4)
            # 2nd dividing line
            pygame.draw.line(self.window, yellow,
                             (0, self.height+self.info_board/2), (self.width, self.height+self.info_board/2), 4)
            # 3rd dividing line
            pygame.draw.line(self.window, yellow,
                             (0, self.height+self.bonus_board), (self.width, self.height+self.bonus_board), 4)
            # 4th dividing line
            pygame.draw.line(self.window, yellow,
                             (0, self.total_height-self.luck_board), (self.width, self.total_height-self.luck_board), 4)

        def get_shortcuts():
            # Info board orange rectangle
            pygame.draw.rect(self.window, orange,
                             (0, self.height+3, self.width, self.info_board/2-3))
            # new game
            game_text = get_plain_text(self.game_font, 'New Game', blue)
            self.window.blit(game_text, (25, self.height + 10))
            # pause game
            game_text = get_plain_text(self.game_font, 'Pause - Space', blue)
            self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                                         self.height + 10))
            # quit game
            game_text = get_plain_text(self.game_font, 'Quit - Esc', blue)
            self.window.blit(game_text, (self.width-(game_text.get_width()+25),
                                         self.height + 10))

        def get_bot_info():
            # Info board red rectangle
            pygame.draw.rect(self.window, red,
                             (0, self.height+self.info_board/2+3, self.width, self.info_board/2-3))
            # points
            game_text = get_text_with_variable(self.game_font, 'Points',
                                               self.bot.points, green)
            self.window.blit(
                game_text, (25, self.height + (self.info_board*0.6)))
            # level
            game_text = get_text_with_variable(self.game_font, 'Level',
                                               self.level, green)
            self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                                         self.height + (self.info_board*0.6)))
            # health
            game_text = get_text_with_variable(self.game_font, 'Health',
                                               self.bot.health, green)
            self.window.blit(game_text, (self.width-(game_text.get_width()+25),
                                         self.height + (self.info_board*0.6)))

        def handle_bonus_text():
            # helper function
            def get_color():
                colors = [dark_grey, dark_grey]
                if self.bonus_coin.x > 0 and not self.bonus_coin.caught:
                    colors = [(random.randint(
                        0, 255), random.randint(0, 255), random.randint(0, 255)), black]

                if self.bonus_coin.caught:
                    if self.bonus_coin.power in ['cupcake', 'add health', 'freeze']:
                        colors = [green, blue]
                    else:
                        colors = [red, orange]

                if self.timer.return_on_frame(30):
                    if self.timer.seconds % 2 == 0:
                        self.random_color = colors[0]
                    else:
                        self.random_color = colors[1]

                # make sure rectangle is dark grey before & after bonus
                if (self.game_over or
                    self.timer.seconds <= 60 or
                        self.timer.seconds in [66, 72]):
                    self.random_color = dark_grey

            # bonus board text if ball / bonus state is active
            def blit_text():
                return self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                                                    self.total_height-self.luck_board-self.bonus_board*0.5-game_text.get_height()/2))

            # background rectangle behind bonus board text with padding
            def blit_text_bg():
                return pygame.draw.rect(self.window, black,
                                        (self.width/2-game_text.get_width()/2-8,
                                         self.total_height-self.luck_board-self.bonus_board*0.5-game_text.get_height() /
                                         2-8,
                                         game_text.get_width()+16,
                                         game_text.get_height()+8))

            get_color()
            # Info board rectangle
            pygame.draw.rect(self.window, (self.random_color),
                             (0, self.height+self.info_board+3, self.width, self.bonus_board-3))

            # bonus record text
            line_one_height = self.total_height - self.bonus_board-self.luck_board + 10
            line_two_height = line_one_height+40
            # text when no ball / no active bonus
            if ((self.bonus_coin.x < 0 and
                not self.bonus_coin.caught) or
                    self.game_over):
                # freeze count
                game_text = get_text_with_variable(
                    self.game_font, 'Freeze', self.bonus_record['freeze'], (0, 255, 0))
                self.window.blit(
                    game_text, (25, line_one_height))
                # cupcake count
                game_text = get_text_with_variable(
                    self.game_font, 'Cupcakes', self.bonus_record['cupcake'], (0, 255, 0))
                self.window.blit(
                    game_text, (self.width*.5-(game_text.get_width()/2), line_one_height))
                # add health count
                game_text = get_text_with_variable(
                    self.game_font, '+ Health', self.bonus_record['add health'], (0, 255, 0))
                self.window.blit(
                    game_text, (self.width-(game_text.get_width()+25),
                                line_one_height))
                # speed count
                game_text = get_text_with_variable(
                    self.game_font, 'Fast', self.bonus_record['speed up'], red)
                self.window.blit(
                    game_text, (25, line_two_height))
                # add monsters count
                game_text = get_text_with_variable(
                    self.game_font, '+ Monsters', self.bonus_record['add monsters'], red)
                self.window.blit(
                    game_text, (self.width*.5-(game_text.get_width()/2), line_two_height))
                # take health count
                game_text = get_text_with_variable(
                    self.game_font, '- Health', self.bonus_record['take health'], red)
                self.window.blit(
                    game_text, (self.width-(game_text.get_width()+25),
                                line_two_height))

            # text when ball is on screen
            game_text = get_plain_text(
                self.heading_font, 'Trick or Treat???', white)

            # if bonus ball is on screen, prompt user to catch it
            if self.bonus_coin.x > -1:
                if not self.game_over:
                    # rectangle behind bonus text
                    blit_text_bg()
                    # game text to window
                    blit_text()

            # display user prompt based on bonus_coin.power
            if self.bonus_coin.caught:
                game_text = get_plain_text(
                    self.heading_font, self.bonus_coin.user_prompt, white)
                if not self.game_over:
                    blit_text_bg()
                    blit_text()

        def handle_luck_board():
            good_luck = self.luck_count['good percentage']/100
            bad_luck = self.luck_count['bad percentage']/100

            # luck board dark grey rectangle
            pygame.draw.rect(self.window, dark_grey,
                             (0, self.total_height-self.luck_board, self.width, self.luck_board))
            # green rect for good luck
            pygame.draw.rect(self.window, green,
                             (0, self.total_height-self.luck_board+2, self.width*good_luck, self.luck_board+2))
            if good_luck + bad_luck > 0:
                word = 'Lucky'
                player_luck = good_luck
                # red rect for bad luck
                pygame.draw.rect(self.window, red,
                                 (self.width*good_luck, self.total_height-self.luck_board+2, self.width, self.luck_board))
                if good_luck >= bad_luck:
                    word = 'Lucky'
                    player_luck = good_luck
                elif bad_luck > good_luck:
                    word = 'Unlucky'
                    player_luck = bad_luck

                # luck board text - You are xx% [lucky / unlucky]
                game_text = self.game_font.render(
                    f"You are {int(player_luck*100)}% {word}!!", True, white)

                # text background with padding
                pygame.draw.rect(self.window, dark_grey,
                                 (self.width/2-game_text.get_width() / 2-8,
                                  self.total_height-self.luck_board*.5 -
                                  game_text.get_height()/2-8,
                                  game_text.get_width()+8,
                                  game_text.get_height()+16))
                # text
                self.window.blit(game_text, (self.width/2-game_text.get_width() /
                                             2, self.total_height-self.luck_board*.5-game_text.get_height()/2))

        def handle_door():
            if all(i.caught == True for i in self.coins):
                if self.door.x < 0:
                    self.door.toggle_visibility()
                    self.door.get_coords(self.bot.y)
            else:
                if self.door.x >= 0:
                    self.door.toggle_visibility()
            self.window.blit(self.door.image, (self.door.x, self.door.y))

        def handle_bonus_ball():
            # helper functions
            def add_health():
                if self.timer.return_on_frame(70):
                    self.bot.add_health()

            def speed_up_monsters():
                for monster in self.monsters:
                    monster.speed_up()

            def toggle_cupcake(cupcake=True):
                for monster in self.monsters:
                    monster.toggle_cupcake(cupcake)

            def add_extra_monsters():
                if self.timer.return_on_frame(70):
                    self.monster_count += 1
                    self.release_monsters()

            def update_luck(type_of_luck: str):
                # update luck counts
                self.luck_count[type_of_luck] += 1
                self.luck_count['total count'] += 1
                # update luck percentages
                if self.luck_count['total count'] > 0:
                    self.luck_count['good percentage'] = int((
                        self.luck_count['good']/self.luck_count['total count'])*100)
                    self.luck_count['bad percentage'] = int(100 -
                                                            self.luck_count['good percentage'])

                    print('good luck: ', self.luck_count['good percentage'])
                    print('bad luck: ', self.luck_count['bad percentage'])

            # bonus coin to screen
            if self.timer.seconds == 60:
                self.bonus_coin.toggle_visibility()
                self.bonus_coin.get_coords(self.bot.y)
                self.bonus_coin.unfreeze()
                self.timer.update_seconds()

            # bonus coin with no contact
            if (self.timer.seconds == 66 and
                    not self.bonus_coin.caught):
                self.timer.update_seconds()
                self.bonus_coin = self.get_bonus_coin()

            # bonus coin caught by Robot
            if self.bonus_coin.hit_robot(self.bot.footprint):
                print('caught bonus coin: ', self.bonus_coin.power)
                update_luck(self.bonus_coin.dict['luck'])
                # Hide coin when caught
                self.bonus_coin.catch_coin()
                self.bonus_coin.toggle_visibility()
                self.bonus_record[self.bonus_coin.power] += 1
                self.timer.seconds = 66

            # if coin is caught
            if self.bonus_coin.caught:
                power_dict = {
                    'freeze': self.freeze_monsters,
                    'speed up': speed_up_monsters,
                    'cupcake': toggle_cupcake,
                    'add monsters': add_extra_monsters,
                    'add health': add_health,
                    'take health': self.take_health,
                }
                # activate bonus ball power
                if self.bonus_coin.power in power_dict:
                    power_dict[self.bonus_coin.power]()

                # end bonus round
                if self.timer.seconds == 72:
                    self.timer.clear_timer()
                    self.unfreeze_monsters()
                    toggle_cupcake(False)
                    self.bonus_coin = self.get_bonus_coin()

            # bonus coin to window
            self.window.blit(self.bonus_coin.image,
                             (self.bonus_coin.x, self.bonus_coin.y))

        # game window will be red to warn that bonus mode will end
        window_color = (red if self.bonus_coin.caught
                        and self.bonus_coin.flash_red
                        and self.timer.seconds == 71
                        else (204, 255, 255))

        self.window.fill(window_color)
        handle_luck_board()

        # Info board text
        get_shortcuts()
        get_bot_info()

        # bonus mode info board
        handle_bonus_text()

        # print door
        handle_door()

        # coins
        for coin in self.coins:
            self.window.blit(coin.image, (coin.x, coin.y))

        # bonus coin
        handle_bonus_ball()

        # dividing lines
        get_dividing_lines()

        # monsters
        for monster in self.monsters:
            self.window.blit(monster.image, (monster.x, monster.y))

        # bot
        self.window.blit(self.bot.image, (self.bot.x, self.bot.y))

        # main window text
        handle_window_text()

        pygame.display.flip()
        self.clock.tick(60)

    def move_bot(self):
        self.bot.move_bot()

        if (self.bot.hit_door(self.door.footprint) and
                all(i.caught == True for i in self.coins)
                ):
            self.level += 1
            self.monster_count += 1
            self.release_coins()
            self.door.get_coords(self.bot.y)
            self.bot.reset_pos()
            self.release_monsters()

    def move_coin(self):
        for coin in self.coins:
            coin.move_object()
            # Coin hits robot & adds point
            if coin.hit_robot(self.bot.footprint):
                self.bot.add_point()
                coin.catch_coin()
                coin.toggle_visibility()

    def move_monster(self):
        for monster in self.monsters:
            monster.move_object()

            if monster.hit_robot(self.bot.footprint):
                # if cupcake BonusCoin was caught, make them edible
                if self.bonus_coin.caught and self.bonus_coin.power == 'cupcake':
                    monster.toggle_visibility()
                    monster.freeze()
                    self.monster_count -= 1
                else:
                    self.bot.take_health()
                    # End game when score hits 0
                    if self.bot.health <= 0:
                        self.bot.health = 0
                        self.game_over = True
                    self.release_monsters()

    def take_health(self):
        if self.timer.return_on_frame(70):
            for i in range(2):
                self.bot.take_health()

    def freeze_monsters(self):
        for monster in self.monsters:
            monster.freeze()

    def unfreeze_monsters(self):
        for monster in self.monsters:
            monster.unfreeze()

    def move_bonus_coin(self):
        self.bonus_coin.move_object()

    def get_bonus_coin(self):
        return BonusCoin(
            self.window_dimensions, 'bonus_coin')

    def toggle_game_over(self):
        if not self.game_over:
            self.game_paused = False if self.game_paused else True

    def release_coins(self):
        self.coins = []
        for i in range(6):
            new_coin = MovingCoin(self.window_dimensions, 'coin')
            new_coin.get_coords(self.height)
            self.coins.append(new_coin)

    def release_monsters(self):
        self.monsters = []
        bot_y = self.bot.y
        for i in range(self.monster_count):
            monster = MovingMonster(self.window_dimensions, 'monster')
            monster.get_coords(bot_y)
            self.monsters.append(monster)

        # release frozen monsters if bonus_coin was caught
        if (self.bonus_coin.caught and
                self.bonus_coin.power == 'freeze'):
            self.freeze_monsters()


if __name__ == '__main__':
    GetCoin()
