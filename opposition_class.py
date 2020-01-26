import pygame
from player_class import Player
from random import randint
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Opposition(Player):
    is_special = False
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self, name):
        super(Opposition, self).__init__()
        self.name = name
        opp_img = pygame.image.load("player-imgs/0_Goblin_Running_000.png").convert()
        self.image = pygame.transform.scale(opp_img, (50, 75))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))

    def update_opps(self):
        num = randint(1,4)
        self.rect = self.get_rect()
        if num == 1:
            self.rect.move_ip(0, -90)
            opp_img = pygame.image.load("player-imgs/0_Goblin_Running_000.png").convert()
            self.image = pygame.transform.scale(opp_img, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if num == 2:
            self.rect.move_ip(0, 90)
            opp_img = pygame.image.load("player-imgs/0_Goblin_Running_000.png").convert()
            self.image = pygame.transform.scale(opp_img, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if num == 3:
            self.rect.move_ip(-90, 0)
            opp_img = pygame.image.load("player-imgs/0_Goblin_Running_000.png").convert()
            self.image = pygame.transform.scale(opp_img, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if num == 4:
            self.rect.move_ip(90, 0)
            self.image = pygame.image.load("player-imgs/0_Goblin_Running_009.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
    
    def update_opps_1(self):
        self.update_opps()

        if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT
    
    def update_opps_1_2(self):
        self.update_opps()

        if self.name == "opp_1":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "opp_2":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT

    def update_opps_1_3(self):
        self.update_opps()

        if self.name == "opp_1":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "opp_3":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT
    
    def update_opps_2_3(self):
        self.update_opps()

        if self.name == "opp_2":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "opp_3":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT

    def update_opps_all(self):
        self.update_opps()

        if self.name == "opp_1":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/3:
                self.rect.bottom = self.SCREEN_HEIGHT/3
        elif self.name == "opp_2":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= self.SCREEN_HEIGHT/3:
                self.rect.top = self.SCREEN_HEIGHT/3
            if self.rect.bottom >= (self.SCREEN_HEIGHT/3) * 2:
                self.rect.bottom = (self.SCREEN_HEIGHT/3) * 2
        elif self.name == "opp_3":
            if self.rect.left < self.SCREEN_WIDTH/2:
                self.rect.left = self.SCREEN_WIDTH/2
            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
            if self.rect.top <= (self.SCREEN_HEIGHT/3) * 2:
                self.rect.top = (self.SCREEN_HEIGHT/3) * 2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT

    def detect_collision(self, ball):
        return self.rect.colliderect(ball.rect)