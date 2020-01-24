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

    def __init__(self):
        super(Hometeam, self).__init__()
        player_img = pygame.image.load("player-imgs/home_team_idle.png").convert()
        self.image = pygame.transform.scale(player_img, (50, 75))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys): 
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -7)
            self.image = pygame.image.load("player-imgs/home_team_idle.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 7)
            self.image = pygame.image.load("player-imgs/home_team_idle.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-9, 0)
            self.image = pygame.image.load("player-imgs/0_Citizen_Walk_006.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(9, 0)
            self.image = pygame.image.load("player-imgs/walk_right.png").convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH/2:
            self.rect.right = SCREEN_WIDTH/2
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    # def special_move(self, is_special):
    #     if self.is_special == True:
    #         if pressed_keys[K_UP]:
    #             self.rect.move_ip(0, -5)
    #         if pressed_keys[K_DOWN]:
    #             self.rect.move_ip(0, 5)
    #         if pressed_keys[K_LEFT]:
    #             self.rect.move_ip(-5, 0)
    #         if pressed_keys[K_RIGHT]:
    #               self.rect.move_ip(5, 0)

        
