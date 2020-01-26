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
opp_list = []
player_list = []
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Hometeam("player")
player2 = Hometeam("player2")
player3 = Hometeam("player3")
player_list.append(player.name)
player_list.append(player2.name)
player_list.append(player3.name)
opp_1 = Opposition("opp_1")
opp_2 = Opposition("opp_2")
opp_3 = Opposition("opp_3")
opp_list.append(opp_1.name)
opp_list.append(opp_2.name)
opp_list.append(opp_3.name)
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
# op2num = randint(400, 725)
# op2num2 = randint(0, 550)
# op3num = randint(400, 725)
# op3num2 = randint(0, 550)

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
    if len(player_list) == 3:
            player.update_players_all(pressed_keys)
            player2.update_players_all(pressed_keys)
            player3.update_players_all(pressed_keys)

    elif len(player_list) == 2:
        if player_list.__contains__("player") and player_list.__contains__("player2"):
            player.update_players_1_2(pressed_keys)
            player2.update_players_1_2(pressed_keys)
        elif player_list.__contains__("player") and player_list.__contains__("player3"):
            player.update_players_1_3(pressed_keys)
            player3.update_players_1_3(pressed_keys)
        elif player_list.__contains__("player2") and player_list.__contains__("player3"):
            player2.update_players_2_3(pressed_keys)
            player3.update_players_2_3(pressed_keys)
    else:
        if player_list.__contains__("player"):
            player.update_players_1(pressed_keys)
        elif player_list.__contains__("player2"):
            player2.update_players_1(pressed_keys)
        else:
            player3.update_players_1(pressed_keys)
 
    if count % 4 == 0:
        if len(opp_list) == 3:
            opp_1.update_opps_all()
            opp_2.update_opps_all()
            opp_3.update_opps_all()

        elif len(opp_list) == 2:
            if opp_list.__contains__("opp_1") and opp_list.__contains__("opp_2"):
                opp_1.update_opps_1_2()
                opp_2.update_opps_1_2()
            elif opp_list.__contains__("opp_1") and opp_list.__contains__("opp_3"):
                opp_1.update_opps_1_3()
                opp_3.update_opps_1_3()
            elif opp_list.__contains__("opp_2") and opp_list.__contains__("opp_3"):
                opp_2.update_opps_2_3()
                opp_3.update_opps_2_3()
        else:
            if opp_list.__contains__("opp_1"):
                opp_1.update_opps_1()
            elif opp_list.__contains__("opp_2"):
                opp_2.update_opps_1()
            else:
                opp_3.update_opps_1()
        

    count += 1
    screen.fill((0, 0, 0))
    
    for entity in all_sprites:
        if isinstance(entity, Hometeam):
            if entity == player:
                screen.blit(entity.image, entity.rect)    
            elif entity == player2:
                screen.blit(entity.image, entity.rect)
            elif entity == player3:
                screen.blit(entity.image, entity.rect)
            
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
            if isinstance(entity, Opposition):
                opp_list.remove(entity.name)
            else:
                player_list.remove(entity.name)
     
        print(entity.name)
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()