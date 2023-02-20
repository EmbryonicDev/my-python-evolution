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
        self.total_height = self.height+self.info_board+self.bonus_board
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
        self.window.fill((204, 255, 255))

        # Info board black rectangle
        pygame.draw.rect(self.window, (0, 0, 0),
                         (0, self.height, self.width, self.info_board))
        # Info board text
        # points
        game_text = self.game_font.render(
            f"Points: {self.bot.points} ", True, (0, 255, 0))
        self.window.blit(game_text, (25, self.height + (self.info_board*0.1)))
        # level
        game_text = self.game_font.render(
            f"Level: {self.level} ", True, (0, 255, 0))
        self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                         self.height + (self.info_board*0.1)))
        # health
        game_text = self.game_font.render(
            f"Health: {self.bot.health} ", True, (0, 255, 0))
        self.window.blit(game_text, (self.width-(game_text.get_width()+25),
                         self.height + (self.info_board*0.1)))
        # new game
        game_text = self.game_font.render(
            "New Game - F2", True, (0, 255, 0))
        self.window.blit(game_text, (25, self.height + (self.info_board*0.5)))
        # pause game
        game_text = self.game_font.render(
            "Pause - Space", True, (0, 255, 0))
        self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                         self.height + (self.info_board*0.5)))
        # quit game
        game_text = self.game_font.render(
            "Quit - Esc", True, (0, 255, 0))
        self.window.blit(game_text, (self.width-(game_text.get_width()+25),
                         self.height + (self.info_board*0.5)))

        # bonus mode info board
        self.handle_bonus_text()

        # print door
        if all(i.caught == True for i in self.coins):
            if self.door.x < 0:
                self.door.toggle_visibility()
                self.door.get_coords(self.bot.y)
        else:
            if self.door.x >= 0:
                self.door.toggle_visibility()
        self.window.blit(self.door.image, (self.door.x, self.door.y))

        # coins
        for coin in self.coins:
            self.window.blit(coin.image, (coin.x, coin.y))

        # bonus coin
        self.handle_bonus_ball()

        # monsters
        for monster in self.monsters:
            self.window.blit(monster.image, (monster.x, monster.y))

        # bot
        self.window.blit(self.bot.image, (self.bot.x, self.bot.y))

        # main window text
        # game over
        if self.game_over:
            game_text = self.heading_font.render(
                'Game Over...', True, (255, 255, 255))
            self.window.blit(game_text, (self.width/2-game_text.get_width() /
                             2, self.height/2-game_text.get_height()/2))
        # game paused
        if self.game_paused:
            game_text = self.heading_font.render(
                'Game Paused...', True, (255, 255, 255))
            self.window.blit(game_text, (self.width/2-game_text.get_width() /
                             2, self.height/2-game_text.get_height()/2))

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

    def handle_bonus_ball(self):
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
            # Hide coin when caught
            self.bonus_coin.catch_coin()
            self.bonus_coin.toggle_visibility()
            self.bonus_record[self.bonus_coin.power] += 1
            self.timer.seconds = 66

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

    def handle_bonus_text(self):
        # new color every second
        self.get_color()
        if self.game_over:
            self.random_color = (0, 0, 0)

        # dividing line
        pygame.draw.line(self.window, (204, 0, 204),
                         (0, self.total_height-self.bonus_board), (self.width, self.total_height-self.bonus_board), 8)

        # Info board rectangle
        pygame.draw.rect(self.window, (self.random_color),
                         (0, self.height+self.info_board, self.width, self.height + self.info_board))

        # text when no ball / no active bonus
        # bonus record text
        line_one_height = self.total_height - self.bonus_board + 10
        line_two_height = line_one_height+40
        if ((self.bonus_coin.x < 0 and
            not self.bonus_coin.caught) or
                self.game_over):
            # freeze count
            game_text = self.get_text(
                self.game_font, 'Freeze', self.bonus_record['freeze'], (0, 255, 0))
            self.window.blit(
                game_text, (25, line_one_height))
            # cupcake count
            game_text = self.get_text(
                self.game_font, 'Cupcakes', self.bonus_record['cupcake'], (0, 255, 0))
            self.window.blit(
                game_text, (self.width*.5-(game_text.get_width()/2), line_one_height))
            # add health count
            game_text = self.get_text(
                self.game_font, '+ Health', self.bonus_record['add health'], (0, 255, 0))
            self.window.blit(
                game_text, (self.width-(game_text.get_width()+25),
                            line_one_height))
            # speed count
            game_text = self.get_text(
                self.game_font, 'Fast', self.bonus_record['speed up'], (255, 0, 0))
            self.window.blit(
                game_text, (25, line_two_height))
            # add monsters count
            game_text = self.get_text(
                self.game_font, '+ Monsters', self.bonus_record['add monsters'], (255, 0, 0))
            self.window.blit(
                game_text, (self.width*.5-(game_text.get_width()/2), line_two_height))
            # take health count
            game_text = self.get_text(
                self.game_font, '- Health', self.bonus_record['take health'], (255, 0, 0))
            self.window.blit(
                game_text, (self.width-(game_text.get_width()+25),
                            line_two_height))

        # text when ball is on screen
        game_text = self.heading_font.render(
            "Trick or Treat???", True, (255, 255, 255))

        # bonus board text if ball / bonus state is active
        def blit_text():
            return self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                                                self.total_height-self.bonus_board*0.5-game_text.get_height()/2))

        # background rectangle behind bonus board text
        def blit_text_bg():
            return pygame.draw.rect(self.window, (0, 0, 0),
                                    (self.width/2-game_text.get_width()/2,
                                     self.total_height-self.bonus_board*0.5-game_text.get_height()/2,
                                     game_text.get_width(),
                                     game_text.get_height()))

        # if bonus ball is on screen, prompt user to catch it
        if self.bonus_coin.x > -1:
            if not self.game_over:
                # rectangle behind bonus text
                blit_text_bg()
                # game text to window
                blit_text()

        # display user prompt based on bonus_coin.power
        if self.bonus_coin.caught:
            game_text = self.heading_font.render(
                self.bonus_coin.user_prompt, True, (255, 255, 255))
            if not self.game_over:
                blit_text_bg()
                blit_text()

    # get text for variable
    def get_text(self, font, text, variable, color: tuple):
        return font.render(
            f"{text}: {variable}", True, color)

    # handle_bonus_text - helper function
    def get_color(self):
        colors = [(0, 0, 0), (0, 0, 0)]
        if self.bonus_coin.x > 0 and not self.bonus_coin.caught:
            colors = [(random.randint(
                0, 255), random.randint(0, 255), random.randint(0, 255)), (0, 0, 0)]

        if self.bonus_coin.caught:
            if self.bonus_coin.power in ['cupcake', 'add health', 'freeze']:
                colors = [(0, 255, 0), (0, 0, 255)]
            else:
                colors = [(255, 0, 0), (255, 188, 0)]

        if self.timer.return_on_frame(30):
            if self.timer.seconds % 2 == 0:
                self.random_color = colors[0]
            else:
                self.random_color = colors[1]

    def toggle_game_over(self):
        if not self.game_over:
            self.game_paused = False if self.game_paused else True

    def release_coins(self):
        self.coins = []
        for i in range(1):
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
