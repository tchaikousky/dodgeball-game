import pygame
from random import randint
from player_class import *
from opposition_class import *
from hometeam_class import *
from ball_stub import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Hometeam()
player2 = Hometeam()
player3 = Hometeam()
opp_1 = Opposition()
opp_2 = Opposition()
opp_3 = Opposition()
ball1 = Ball()
enemies = pygame.sprite.Group()
enemies.add(opp_1)
enemies.add(opp_2)
enemies.add(opp_3)
all_sprites = pygame.sprite.Group()
all_sprites.add(opp_1)
all_sprites.add(opp_2)
all_sprites.add(opp_3)
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
all_balls = pygame.sprite.Group()
all_balls.add(ball1)

# Run until the user asks to quit
running = True
count = 0
num1 = randint(400, 550)
num2 = randint(0, 550)
op2num = randint(400, 725)
op2num2 = randint(0, 550)
op3num = randint(400, 725)
op3num2 = randint(0, 550)

while running:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                break
        elif event.type == QUIT:
            running = False
            break

    #Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on keypresses
    player.update(pressed_keys)
 
    if count % 4 == 0:
        opp_1.update_opps()
        opp_2.update_opps()
        opp_3.update_opps()

    count += 1
    screen.fill((0, 0, 0))
    
    for entity in all_sprites:
        if isinstance(entity, Hometeam):
            if entity == player:
                screen.blit(entity.image, entity.rect)    
            elif entity == player2:
                screen.blit(entity.image, [200,100, 50, 75])
            elif entity == player3:
                screen.blit(entity.image, [150,375, 50, 75])
            
        elif isinstance(entity, Opposition):
            if entity == opp_1:
                # print("dog")
                screen.blit(entity.image, entity.rect)        
            elif entity == opp_2:
                screen.blit(entity.image, entity.rect)      
            elif entity == opp_3:
                # print("mouse")
                screen.blit(entity.image, entity.rect)
            print(entity.get_rect())

        screen.blit(ball1.surf, ball1.rect)
        if entity.detect_collision(ball1) == True:
            entity.kill()

    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()