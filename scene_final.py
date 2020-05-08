import pygame
# import random
# from player_class import *
from random import randint
from player_class import *
from opposition_class import *
from hometeam_class import *
from ball_stub import *
from level_class import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
pygame.font.init()
pygame.font.SysFont("Arial",115)

pygame.mixer.init(48000, -16, 1, 1024)




from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    QUIT,
)



# Set up the drawing window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
level_count = 1
game_over = False
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
ball1 = Ball("ball1")
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
all_sprites.add(ball1)

# Set up colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
off_white = (200,200,200) 
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gameText = pygame.font.SysFont("Arial",115)

game_title = pygame.display.set_caption("DODGEBALL 2k20")

# Definining the ball function
def new_ball(all_balls):
    b = Ball("1")
    all_balls.add(b)
    all_sprites.add(b)

# Defining text objects?
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def black_text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# This is the text for the title on the intro screen
def message_display(text):
    gameText = pygame.font.SysFont("Arial",75)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/2)))
    screen.blit(TextSurf, TextRect)

# This is the message for the space key funcitonality on the intro screen
def continue_message_display(text):
    gameText = pygame.font.SysFont("Arial",25)
    TextSurf, TextRect = text_objects(text, gameText)
    TextRect.center = ((round(SCREEN_WIDTH/2)),(round(SCREEN_HEIGHT/1.5)))
    screen.blit(TextSurf, TextRect)

# New ball funciton
for i in range(1):
    new_ball(all_balls)

# Loading background graphics
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()
background_rect = background.get_rect()

# player = Player()
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

pygame.init()

intro = True
while intro:
    screen.fill(black)
    message_display("DODGEBALL 2k20")
    continue_message_display("PRESS THE SPACE KEY TO CONTINUE")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                intro = False
                pygame.quit()
                quit()
                break
        elif event.type == QUIT:
            intro = False
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intro = False
                break

pygame.mixer.init()
in_game_song = pygame.mixer.Sound(path.join(snd_dir, "hot_wav_version.wav"))
in_game_song.set_volume(0.1)
in_game_song.play()


running = True
count = 0
def isGameOver(player_count):
    if player_count == 0:
        game_over = True
    else:
        game_over = False
    return game_over

def draw_scene(level_count):
    screen.fill((0, 0, 0))
    screen.blit(level.image, level.rect)
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
                screen.blit(entity.image, entity.rect)        
            elif entity == opp_2:
                screen.blit(entity.image, entity.rect)      
            elif entity == opp_3:
                screen.blit(entity.image, entity.rect)

        screen.blit(ball1.image, ball1.rect)     
        # hits = pygame.sprite.spritecollide(entity, all_balls, True)
        if ball1.detect_collision(entity) == True:
            entity.kill()
            ball1.kill()
            if isinstance(entity, Opposition):
                opp_list.remove(entity.name)
                if len(opp_list) == 0:
                    player_list.clear
                
            elif isinstance(entity, Hometeam):
                player_list.remove(entity.name)
                if len(player_list) == 0:
                    level_count = 10
                    
        # print(entity.name)

    #Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on keypresses
     
    if len(player_list) == 3:
            player.update_players_all(pressed_keys)
            player2.update_players_all(pressed_keys)
            player3.update_players_all(pressed_keys)
            ball1.update(pressed_keys, all_balls)

    elif len(player_list) == 2:
        if player_list.__contains__("player") and player_list.__contains__("player2"):
            player.update_players_1_2(pressed_keys)
            player2.update_players_1_2(pressed_keys)
            ball1.update(pressed_keys, all_balls)

        elif player_list.__contains__("player") and player_list.__contains__("player3"):
            player.update_players_1_3(pressed_keys)
            player3.update_players_1_3(pressed_keys)
            ball1.update(pressed_keys, all_balls)

        elif player_list.__contains__("player2") and player_list.__contains__("player3"):
            player2.update_players_2_3(pressed_keys)
            player3.update_players_2_3(pressed_keys)
            ball1.update(pressed_keys, all_balls)

    else:
        if player_list.__contains__("player"):
            player.update_players_1(pressed_keys)
            ball1.update(pressed_keys, all_balls)

        elif player_list.__contains__("player2"):
            player2.update_players_1(pressed_keys)
            ball1.update(pressed_keys, all_balls)

        else:
            player3.update_players_1(pressed_keys)
            ball1.update(pressed_keys, all_balls)

 
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

while running:
    
    game_over = isGameOver(len(player_list))
    if game_over == False:
        if level_count == 1:
            # level = Level("player-imgs/basketball_court.jpg", [0,0])
            level = Level("img/fancy-court.png", [0,0])

            if len(opp_list) == 0:
                for sprite in all_sprites:
                    sprite.kill()
                level_count += 1
            draw_scene(1)

        else: 
            # player_count = 0
            level = Level("player-imgs/game_over.png", [0,0])
            for opp in enemies:
                opp.kill()
            ball1.kill()
            draw_scene(100)
    else: 
        level = Level("player-imgs/game_over.png", [0,0])
        for opp in enemies:
            opp.kill()
        ball1.kill   
        draw_scene(100)

    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_ball(all_balls)
        elif event.type == QUIT:
            running = False
            break

    count += 1
    
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
quit()
#################################################################################################################
# running = True
# while running:

#     # Did the user click the window close button? ************************
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#                 break
#         elif event.type == QUIT:
#             running = False
#             break

#     #Get all the keys currently pressed ************************
#     pressed_keys = pygame.key.get_pressed()
#     # Update the player sprite based on keypresses ************************
#     player.update(pressed_keys)
#         # Fill the background with white ************************
#     screen.fill(black)
#     screen.blit(background, background_rect)
#     in_game_song.play()

#     for entity in all_sprites:
#         screen.blit(entity.surf, entity.rect)

#     surf = pygame.Surface((50,50))
#     surf.fill((255,33,127))

#     surf_center = (
#         (SCREEN_WIDTH-surf.get_width())/2,
#         (SCREEN_HEIGHT -surf.get_height())/2,
#     )


#     screen.blit(player.surf, player.rect)
#     # Flip the display ************************
#     pygame.display.flip()

# # Done! Time to quit. ************************
# pygame.quit()
# quit()
##############################################################################################