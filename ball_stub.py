import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
            super(Ball, self).__init__()
            self.surf = pygame.Surface((50,50))
            self.surf.fill((255,255,255))
            # self.surf.fill((0,0,0))
            self.rect = self.surf.get_rect()

    def draw_ball(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        