import pygame
import random


def get_image(image: str):
    return pygame.image.load(image+'.png')


class ScreenObject:
    def __init__(self, screen_dimensions: list, image: str):
        self.image = get_image(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.screen_width = screen_dimensions[0]
        self.screen_height = screen_dimensions[1]
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, self.screen_height - self.height)

    def toggle_visibility(self):
        self.x *= -1
        self.y *= -1

    # release objects on opposite side of bot on contact
    def get_coords(self, bot_y: str):
        self.x = random.randint(0, self.screen_width-self.width)
        self.y = (random.randint(0+self.height, self.screen_height*0.2)
                  if bot_y > self.screen_height / 2
                  else random.randint(self.screen_height*0.8,
                                      self.screen_height-self.height))


class MovingObject(ScreenObject):
    def __init__(self, screen_dimensions: list, image: str):
        ScreenObject.__init__(self, screen_dimensions, image)
        self.choices = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
        self.x_speed = random.choice(self.choices)
        self.y_speed = random.choice(self.choices)

    def move_object(self):
        if self.x <= 0 or self.x + self.width >= self.screen_width:
            self.x_speed *= -1
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.y_speed *= -1

        self.x += self.x_speed
        self.y += self.y_speed

    def hit_robot(self, bot_x: str, bot_y: str):
        return (bot_x <= self.x <= bot_x + self.width and
                bot_y <= self.y <= bot_y + self.height)

    def speed_up(self):
        self.x_speed = 14 if self.x_speed > 0 else -14
        self.y_speed = 14 if self.y_speed > 0 else -14

    def freeze(self):
        self.x_speed, self.y_speed = 0, 0

    def unfreeze(self):
        self.x_speed, self.y_speed = random.choice(
            self.choices), random.choice(self.choices)

    def toggle_cupcake(self, cupcake: bool):
        self.image = get_image('cupcake' if cupcake else 'monster')


class MovingCoin(MovingObject):
    def __init__(self, screen_dimensions, image):
        MovingObject.__init__(self, screen_dimensions, image)
        self.caught = False

    def catch_coin(self):
        self.caught = True


class BonusCoin(MovingCoin):
    def __init__(self, screen_dimensions: list, image: str):
        MovingCoin.__init__(self, screen_dimensions, image)
        # ['eat', 'kill', 'freeze', 'add health', 'multiply', 'invincible']

        self.dict = random.choice(
            [
                # {'power': 'freeze', 'user_prompt': 'Ghosts are Frozen'},
                # {'power': 'speed up', 'user_prompt': 'Super Fast Ghosts! Be Careful!'},
                {'power': 'cupcake', 'user_prompt': 'Eat the Cupcakes!'}
            ])
        self.power = self.dict['power']
        self.user_prompt = self.dict['user_prompt']
        self.freeze()
        self.toggle_visibility()
        print(self.power)


class Robot(ScreenObject):
    def __init__(self, screen_dimensions, image):
        ScreenObject.__init__(self, screen_dimensions, image)
        self.health = 100
        self.speed = 8
        self.points = 0
        self.to_left = False
        self.to_right = False
        self.to_up = False
        self.to_down = False
        self.reset_pos()

    def reset_pos(self):
        self.x = 0
        self.y = self.screen_height - self.height

    def add_point(self):
        self.points += 1

    def take_health(self):
        self.health -= 1

    def move_bot(self):
        if self.to_right and self.x <= self.screen_width - self.width:
            self.x += self.speed
        if self.to_left and self.x >= 0:
            self.x -= self.speed
        if self.to_down and self.y <= self.screen_height - self.height:
            self.y += self.speed
        if self.to_up and self.y >= 0:
            self.y -= self.speed

    def hit_door(self, door_x, door_y):
        return (self.x <= door_x <= self.x + self.width and
                self.y <= door_y <= self.y + self.height)


class Timer:
    def __init__(self):
        self.frame_counter = 0
        self.seconds = 55

    def clear_timer(self):
        self.seconds = 55
        self.frame_counter = 0

    def add_counter(self):
        self.frame_counter += 1
        if self.frame_counter % 60 == 0:
            self.update_seconds()

    def update_seconds(self):
        print(self.seconds)
        self.seconds += 1
        if self.seconds == 73:
            self.clear_timer()


class GetCoin:
    def __init__(self):
        pygame.init()

        # Window
        self.width = 1000
        self.height = 900
        self.info_board = 100
        self.bonus_board = 135
        self.total_height = self.height+self.info_board+self.bonus_board
        self.window = pygame.display.set_mode(
            (self.width, self.height+self.info_board+self.bonus_board))
        pygame.display.set_caption('Coin Chaser')

        self.game_font = pygame.font.SysFont('Arial', 36)
        self.heading_font = pygame.font.SysFont('Arial', 72)
        self.door = ScreenObject([self.width, self.height], 'door')
        self.clock = pygame.time.Clock()
        self.new_game()
        self.main_loop()

    def new_game(self):
        self.timer = Timer()
        self.random_color = (random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        self.bonus_coin = self.get_bonus_coin()
        self.game_over = False
        self.game_paused = False
        self.level = 1
        self.monster_count = 1
        self.monsters = []
        self.bot = Robot([self.width, self.height], 'robot')
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.bot.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.bot.to_right = True
                if event.key == pygame.K_UP:
                    self.bot.to_up = True
                if event.key == pygame.K_DOWN:
                    self.bot.to_down = True
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.game_paused = True if self.game_paused == False else False
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.bot.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.bot.to_right = False
                if event.key == pygame.K_UP:
                    self.bot.to_up = False
                if event.key == pygame.K_DOWN:
                    self.bot.to_down = False

            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((255, 0, 0))

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
        if self.bot.hit_door(self.door.x, self.door.y):
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
            if coin.hit_robot(self.bot.x, self.bot.y):
                self.bot.add_point()
                coin.catch_coin()
                coin.toggle_visibility()
                print('points: ', self.bot.points)
                print('level: ', self.level)

    def move_monster(self):
        for monster in self.monsters:
            monster.move_object()

            if monster.hit_robot(self.bot.x, self.bot.y):
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

    def toggle_cupcake(self, cupcake: bool):
        for monster in self.monsters:
            monster.toggle_cupcake(cupcake)

    def speed_up_monsters(self):
        for monster in self.monsters:
            monster.speed_up()

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
            [self.width, self.height], 'bonus_coin')

    def get_color(self):
        if self.timer.frame_counter % 60 == 0:
            self.random_color = (random.randint(
                0, 255), random.randint(0, 255), random.randint(0, 255))

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
        if self.bonus_coin.hit_robot(self.bot.x, self.bot.y):
            # Hide coin when caught
            print('caught bonus coin: ', self.bonus_coin.power)
            self.bonus_coin.catch_coin()
            self.bonus_coin.toggle_visibility()
            self.timer.seconds = 66

        # if coin is caught
        if self.bonus_coin.caught:
            if self.bonus_coin.power == 'freeze':
                self.freeze_monsters()
            if self.bonus_coin.power == 'speed up':
                self.speed_up_monsters()

            # end bonus round
            if self.timer.seconds == 72:
                self.timer.clear_timer()
                self.unfreeze_monsters()
                self.bonus_coin = self.get_bonus_coin()

        # bonus coin to window
        self.window.blit(self.bonus_coin.image,
                         (self.bonus_coin.x, self.bonus_coin.y))

    def handle_bonus_text(self):
        # new color every second
        self.get_color()
        # random color if bonus_coin is caught or is not on screen, else, black
        board_color = (self.random_color
                       if self.bonus_coin.x > 0
                       or self.bonus_coin.caught
                       else (
                           0*3))

        # Info board rectangle
        pygame.draw.rect(self.window, (board_color),
                         (0, self.height+self.info_board, self.width, self.height + self.info_board))

        # text when ball is on screen
        game_text = self.heading_font.render(
            "Catch Bonus Ball", True, (255, 255, 255))

        def blit_text():
            return self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                                                self.height + self.info_board + (self.info_board*0.35)))

        def blit_text_bg():
            return pygame.draw.rect(self.window, (0, 0, 0), (self.width/2-game_text.get_width()/2, self.total_height - self.bonus_board/2 - game_text.get_height()/2, game_text.get_width(), game_text.get_height()))

        # if bonus ball is on screen, prompt user to catch it
        if self.bonus_coin.x > -1:
            # rectangle behind bonus text
            blit_text_bg()
            # game text to window
            blit_text()

        if self.bonus_coin.caught:
            game_text = self.heading_font.render(
                self.bonus_coin.user_prompt, True, (255, 255, 255))
            blit_text_bg()
            blit_text()

    def release_coins(self):
        print('coins released')
        self.coins = []
        for i in range(5):
            new_coin = MovingCoin([self.width, self.height], 'coin')
            self.coins.append(new_coin)

    def release_monsters(self):
        self.monsters = []
        bot_y = self.bot.y
        for i in range(self.monster_count):
            monster = MovingObject([self.width, self.height], 'monster')
            print('monster height: ', monster.height)
            monster.get_coords(bot_y)
            self.monsters.append(monster)

        # release frozen monsters if bonus_coin was caught
        if (self.bonus_coin.caught and
                self.bonus_coin.power == 'freeze'):
            self.freeze_monsters()


if __name__ == '__main__':
    GetCoin()
