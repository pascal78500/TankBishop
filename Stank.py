# define the class tank
import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tankr.png")
        self.screen = screen
        self.rect = self.image.get_rect()
        self.x = 100
        self.vx = 1
    def update(self):
        self.x +=self.vx
        if self.x > self.screen.get_width()+27:
            self.reset()
        self.rect.center = (self.x, 227)

    def reset(self):
        self.x = -7