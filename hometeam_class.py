import pygame
from player_class import Player
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Hometeam(Player):
    is_special = False
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self, name):
        super(Hometeam, self).__init__()
        self.name = name 
        transColor = self.image.get_at((0,0))
        player_img = pygame.image.load("player-imgs/home_team_idle.png").convert()
        self.image = pygame.transform.scale(player_img, (50, 75))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()

    def update_players(self, pressed_keys): 
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -15)
            self.image = pygame.image.load("player-imgs/home_team_idle.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 15)
            self.image = pygame.image.load("player-imgs/home_team_idle.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
            self.image = pygame.image.load("player-imgs/0_Citizen_Walk_006.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)
            self.image = pygame.image.load("player-imgs/walk_right.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.image.set_colorkey(self.image.get_at((0,0)))

    def update_players_1(self, pressed_keys):
        self.update_players(pressed_keys)

        if self.rect.left < 0:
                self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH/2:
            self.rect.right = self.SCREEN_WIDTH/2
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT
    
    def update_players_1_2(self, pressed_keys):
        self.update_players(pressed_keys)

        if self.name == "player":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "player2":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT

    def update_players_1_3(self, pressed_keys):
        self.update_players(pressed_keys)

        if self.name == "player":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "player3":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT
    
    def update_players_2_3(self, pressed_keys):
        self.update_players(pressed_keys)

        if self.name == "player2":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/2:
                self.rect.bottom = self.SCREEN_HEIGHT/2
        elif self.name == "player3":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= self.SCREEN_HEIGHT/2:
                self.rect.top = self.SCREEN_HEIGHT/2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT

    def update_players_all(self, pressed_keys):
        self.update_players(pressed_keys)

        if self.name == "player":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.SCREEN_HEIGHT/3:
                self.rect.bottom = self.SCREEN_HEIGHT/3
        if self.name == "player2":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= self.SCREEN_HEIGHT/3:
                self.rect.top = self.SCREEN_HEIGHT/3
            if self.rect.bottom >= (self.SCREEN_HEIGHT/3) * 2:
                self.rect.bottom = (self.SCREEN_HEIGHT/3) * 2
        if self.name == "player3":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.SCREEN_WIDTH/2:
                self.rect.right = self.SCREEN_WIDTH/2
            if self.rect.top <= (self.SCREEN_HEIGHT/3) * 2:
                self.rect.top = (self.SCREEN_HEIGHT/3) * 2
            if self.rect.bottom >= self.SCREEN_HEIGHT:
                self.rect.bottom = self.SCREEN_HEIGHT    
