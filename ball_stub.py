import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
            super(Ball, self).__init__()
            num1 = 400 - 30
            num2 = 300 -30
            self.surf = pygame.Surface((35,35))
            self.surf.fill((255,255,255))
            # self.surf.fill((0,0,0))
            self.rect = (num1, num2, 35, 55)

    def draw_ball(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
    
    def get_rect(self):
        return self.rect