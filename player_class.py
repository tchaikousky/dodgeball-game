import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):   
    def __init__(self):
        super(Player, self).__init__()
        player_img = pygame.image.load("player-imgs/0_Citizen_Idle_000.png").convert()
        self.image = pygame.transform.scale(player_img, (50, 75))
        self.rect = self.image.get_rect()
    
    def get_rect(self):
        return self.rect

    def detect_collision(self, ball):
        return self.rect.colliderect(ball.rect)
    