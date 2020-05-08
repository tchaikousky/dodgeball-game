#imports and CONSTANTS

#imports
import pygame 
import random
# from player_class import *
from os import path
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)


img_dir = path.join(path.dirname(__file__), 'img')
# ball_img = pygame.image.load(path.join(img_dir, "sphere-11.png"))

#CONST
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
    # sprite for the Player
    WIDTH = 800
    def __init__(self, name):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load("img\sphere-11.png").convert()
        self.image = pygame.transform.scale(self.image, (25,25))
        self.name = name
        transColor = self.image.get_at((0,0))
        self.image.set_colorkey(transColor)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        #draw a circle
        self.radius = int(self.rect.width * .85/ 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # center the sprite on the screen
        self.rect.centerx = int(WIDTH / 2.5)
        self.rect.bottom = int(HEIGHT / 2.5)
        self.speedx = -10

    def update(self, pressed_keys, group_name):
            # any code here will happen every time the game loop updates
        if self.rect.centerx > self.WIDTH:
            self.kill()
            new_ball(group_name)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.rect.x -= self.speedx
    def detect_collision(self, entity):
        return self.rect.colliderect(entity.rect)

def new_ball(group_name):
    b = Ball("1")
    group_name.add(b)
    group_name.add(b)
        
    

        

    




# for i in range(1):
#     new_ball()

# Game loop
# running = True
# while running:
#     # keep loop running at the right speed
#     clock.tick(FPS)
#     # Process input (events)
#     for event in pygame.event.get():
#         # check for closing window
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 new_ball()