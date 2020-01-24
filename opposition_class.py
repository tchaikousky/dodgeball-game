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

    def __init__(self):
        super(Opposition, self).__init__()
        random1 = randint(350, 750)
        random2 = randint(0, 550)
        opp_img = pygame.image.load("player-imgs/0_Goblin_Running_000.png").convert()
        self.image = pygame.transform.scale(opp_img, (50, 75))
        # self.surf.fill((0,0,0))
        self.rect = self.image.get_rect()
        # self.image.rect = [random1,random2, 50, 75]

    def update_opps(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        num = randint(1,4)
        self.rect = self.get_rect()
        if num == 1:
            self.rect.move_ip(0, -20)
        if num == 2:
            self.rect.move_ip(0, 20)
        if num == 3:
            self.rect.move_ip(-20, 0)
        if num == 4:
            self.rect.move_ip(20, 0)

        if self.rect.left < SCREEN_WIDTH/2:
            self.rect.left = SCREEN_WIDTH/2
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
    def detect_collision(self, ball):
        return self.rect.colliderect(ball.rect)