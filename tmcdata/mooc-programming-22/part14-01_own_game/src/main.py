import pygame
import random


class MovingObject:
    def __init__(self, x, y, directions):
        self.x = x
        self.y = y
        self.x_speed = directions[0]
        self.y_speed = directions[1]


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

        self.to_left, self.to_right, self.to_up, self.to_down = False, False, False, False
        self.clock = pygame.time.Clock()

        self.load_images()
        self.robot_height = self.images['robot'].get_height()
        self.robot_width = self.images['robot'].get_width()
        self.coin_width = self.images['coin'].get_width()
        self.new_game()
        self.main_loop()

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            self.move_coin()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_UP:
                    self.to_up = True
                if event.key == pygame.K_DOWN:
                    self.to_down = True
                if event.key == pygame.K_F2:
                    self.new_game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False

            if event.type == pygame.QUIT:
                exit()

        self.move_bot()

    def draw_window(self):
        self.window.fill((0)*3)
        self.window.blit(self.images['robot'], self.robot_pos)

        for coin in self.coins:
            self.window.blit(self.images['coin'],
                             (coin.x, coin.y))

        pygame.display.flip()
        self.clock.tick(60)

    def move_bot(self):
        if self.to_right and self.robot_pos[0] <= self.width - self.robot_width:
            self.robot_pos[0] += 2
        if self.to_left and self.robot_pos[0] >= 0:
            self.robot_pos[0] -= 2
        if self.to_down and self.robot_pos[1] <= self.height - self.robot_height:
            self.robot_pos[1] += 2
        if self.to_up and self.robot_pos[1] >= 0:
            self.robot_pos[1] -= 2

    def move_coin(self):
        for coin in self.coins:
            if coin.x <= 0 or coin.x + self.coin_width >= self.width:
                coin.x_speed *= -1
            if coin.y <= 0 or coin.y + self.coin_width >= self.height:
                coin.y_speed *= -1

            coin.x += coin.x_speed
            coin.y += coin.y_speed

    def get_direction(self):
        return [random.choice(
            [-8, 8]), random.choice((-8, 8))]

    def load_images(self):
        self.images = {}
        for name in ['coin', 'robot', 'door', 'monster']:
            self.images[name] = pygame.image.load(name+'.png')

    def release_coins(self):
        self.coins = []
        for i in range(5):
            new_coin = MovingObject(random.randint(
                0, self.width - self.coin_width), random.randint(
                0, self.height - self.coin_width), self.get_direction())
            self.coins.append(new_coin)

    def new_game(self):
        self.robot_pos = [0, self.height - self.robot_height]
        self.release_coins()


if __name__ == '__main__':
    GetCoin()
