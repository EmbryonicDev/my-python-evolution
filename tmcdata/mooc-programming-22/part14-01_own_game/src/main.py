import pygame
import random


def get_image(image: str):
    return pygame.image.load(image+'.png')


class MovingObject:
    def __init__(self, screen_dimensions: list, image: str):
        self.x_speed = random.choice([-8, 8])
        self.y_speed = random.choice([-8, 8])
        self.image = get_image(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, screen_dimensions[0] - self.width)
        self.y = random.randint(0, screen_dimensions[1] - self.height)


class MovingCoin(MovingObject):
    def __init__(self, screen_dimensions, image):
        MovingObject.__init__(self, screen_dimensions, image)
        self.caught = False


class Door:
    def __init__(self, screen_dimensions: list):
        self.visible = False
        self.image = get_image('door')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, screen_dimensions[0] - self.width)
        self.y = random.randint(0, screen_dimensions[1] - self.height)


class Robot:
    def __init__(self, screen_height: int):
        self.lives = 4
        self.speed = 2
        self.points = 0
        self.image = get_image('robot')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 0
        self.y = screen_height - self.height
        self.to_left = False
        self.to_right = False
        self.to_up = False
        self.to_down = False


class GetCoin:
    def __init__(self):
        pygame.init()

        # Window
        self.width = 1000
        self.height = 900
        self.info_board = 100
        self.window = pygame.display.set_mode(
            (self.width, self.height+self.info_board))
        pygame.display.set_caption('Coin Chaser')

        self.door = self.get_door()
        self.clock = pygame.time.Clock()
        self.new_game()
        self.main_loop()

    def get_door(self):
        return Door([self.width, self.height])

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            self.move_coin()
            self.move_bot()

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
        self.window.fill((0)*3)

        # print door
        if all(i.caught == True for i in self.coins):
            self.window.blit(self.door.image, (self.door.x, self.door.y))

        for coin in self.coins:
            if not coin.caught:
                self.window.blit(coin.image,
                                 (coin.x, coin.y))

        pygame.display.flip()
        self.clock.tick(60)

    def move_bot(self):
        if self.bot.to_right and self.bot.x <= self.width - self.bot.width:
            self.bot.x += 2
        if self.bot.to_left and self.bot.x >= 0:
            self.bot.x -= 2
        if self.bot.to_down and self.bot.y <= self.height - self.bot.height:
            self.bot.y += 2
        if self.bot.to_up and self.bot.y >= 0:
            self.bot.y -= 2

    def move_coin(self):
        for coin in self.coins:
            if not coin.caught:
                if coin.x <= 0 or coin.x + coin.width >= self.width:
                    coin.x_speed *= -1
                if coin.y <= 0 or coin.y + coin.height >= self.height:
                    coin.y_speed *= -1

                # Coin hits robot & adds point
                if (self.bot.x <= coin.x <= self.bot.x + self.bot.width and
                        self.bot.y <= coin.y <= self.bot.y + self.bot.height):
                    self.bot.points += 1
                    coin.caught = True
                    print('points: ', self.bot.points)

                coin.x += coin.x_speed
                coin.y += coin.y_speed

    def release_coins(self):
        self.coins = []
        for i in range(5):
            new_coin = MovingCoin([self.width, self.height], 'coin')
            self.coins.append(new_coin)

    def new_game(self):
        self.bot = Robot(self.height)
        self.release_coins()


if __name__ == '__main__':
    GetCoin()
