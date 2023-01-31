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
        

class StaticObject(ScreenObject):
    def __init__(self, screen_dimensions: list, image: str):
        ScreenObject.__init__(self, screen_dimensions, image)
        self.new_location()
                
    def toggle_visibility(self):
        self.x *= -1
        self.y *= -1
        
    def new_location(self):
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(self.height, self.screen_height - self.height)  
                
class MovingObject(ScreenObject):
    def __init__(self, screen_dimensions: list, image: str):
        ScreenObject.__init__(self, screen_dimensions, image)
        self.choices = range(-7, 7)
        self.x_speed = random.choice(self.choices)
        self.y_speed = random.choice(self.choices)
        self.new_location()        
        
    def new_location(self):
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, self.screen_height - self.height) 
        
class MovingMonster(MovingObject):
    def __init__(self, screen_dimensions, image):
        MovingObject.__init__(self, screen_dimensions, image)
        
    # release monsters on opposite side of bot on contact
    def get_coords(self, bot_y: str):
        self.x = random.randint(0, self.screen_width-self.width)
        self.y = (random.randint(0, self.screen_height*0.2)
                         if bot_y > self.height / 2
                         else random.randint(self.height*0.8, self.screen_height-monster.height))
                     

class MovingCoin(MovingObject):
    def __init__(self, screen_dimensions, image):
        MovingObject.__init__(self, screen_dimensions, image)
        self.caught = False
        
    def catch_coin(self):
        self.caught = True
        
        
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


class GetCoin:
    def __init__(self):
        pygame.init()

        # Window
        self.width = 1000
        self.height = 900
        self.info_board = 200
        self.window = pygame.display.set_mode(
            (self.width, self.height+self.info_board))
        pygame.display.set_caption('Coin Chaser')

        self.game_font = pygame.font.SysFont('Arial', 36)
        self.end_font = pygame.font.SysFont('Arial', 72)
        self.door = StaticObject([self.width, self.height], 'door')
        self.clock = pygame.time.Clock()
        self.new_game()
        self.main_loop()

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            if not self.game_over and not self.game_paused:
                self.move_coin()    
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
        self.window.blit(game_text, (25, self.height + (self.info_board*0.35)))
        # pause game
        game_text = self.game_font.render(
            "Pause - Space", True, (0, 255, 0))
        self.window.blit(game_text, (self.width*.5-(game_text.get_width()/2),
                         self.height + (self.info_board*0.35)))     
        # quit game
        game_text = self.game_font.render(
            "Quit - Esc", True, (0, 255, 0))
        self.window.blit(game_text, (self.width-(game_text.get_width()+25),
                         self.height + (self.info_board*0.35)))

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
            if not coin.caught:
                self.window.blit(coin.image,
                                 (coin.x, coin.y))

        # monsters
        for monster in self.monsters:
            self.window.blit(monster.image, (monster.x, monster.y))

        # bot
        self.window.blit(self.bot.image, (self.bot.x, self.bot.y))

        # main window text
        # game over
        if self.game_over:
            game_text = self.end_font.render('Game Over...', True, (255, 255, 255))
            self.window.blit(game_text, (self.width/2-game_text.get_width()/2, self.height/2-game_text.get_height()/2))
        # game paused
        if self.game_paused:
            game_text = self.end_font.render('Game Paused...', True, (255, 255, 255))
            self.window.blit(game_text, (self.width/2-game_text.get_width()/2, self.height/2-game_text.get_height()/2))           

        pygame.display.flip()
        self.clock.tick(60)
        

    def move_bot(self):
        if self.bot.to_right and self.bot.x <= self.width - self.bot.width:
            self.bot.x += self.bot.speed
        if self.bot.to_left and self.bot.x >= 0:
            self.bot.x -= self.bot.speed
        if self.bot.to_down and self.bot.y <= self.height - self.bot.height:
            self.bot.y += self.bot.speed
        if self.bot.to_up and self.bot.y >= 0:
            self.bot.y -= self.bot.speed

        # robot hits door
        if (self.bot.x <= self.door.x <= self.bot.x + self.bot.width and
                self.bot.y <= self.door.y <= self.bot.y + self.bot.height):
            self.level += 1
            self.release_coins()
            self.door.new_location()
            self.bot.reset_pos()
            self.release_monsters()

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
                    self.bot.add_point()
                    coin.catch_coin()
                    print('points: ', self.bot.points)
                    print('level: ', self.level)

                coin.x += coin.x_speed
                coin.y += coin.y_speed

    def move_monster(self):
        for monster in self.monsters:
            if monster.x <= 0 or monster.x + monster.width >= self.width:
                monster.x_speed *= -1
            if monster.y <= 0 or monster.y + monster.height >= self.height:
                monster.y_speed *= -1

            # monster hits robot and takes a health point
            if (self.bot.x <= monster.x <= self.bot.x + self.bot.width and
                    self.bot.y <= monster.y <= self.bot.y + self.bot.height):
                self.bot.take_health()
                # End game when score hits 0
                if self.bot.health <= 0:
                    self.bot.health = 0
                    self.game_over = True
                
                print('health remaining: ', self.bot.health)
                self.release_monsters()

            monster.x += monster.x_speed
            monster.y += monster.y_speed

    def release_coins(self):
        print('coins released')
        self.coins = []
        for i in range(1):
            new_coin = MovingCoin([self.width, self.height], 'coin')
            self.coins.append(new_coin)

    def release_monsters(self): 
        self.monsters = []
        for i in range(self.level):
            monster = MovingMonster([self.width, self.height], 'monster')
            monster.get_coords(self.bot.y)
            self.monsters.append(monster)

    def new_game(self):
        self.game_over = False
        self.game_paused = False
        self.level = 1
        self.monsters = []
        self.bot = Robot([self.width, self.height], 'robot')
        self.release_coins()
        self.release_monsters()


if __name__ == '__main__':
    GetCoin()
