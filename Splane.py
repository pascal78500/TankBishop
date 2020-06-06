# plane class
import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect()

        self.x = self.screen.get_width()
        self.y = 10
        self.vx = -2

    def update(self):
        self.x += self.vx
        if self.x < -25:
            self.reset()
        self.rect.center = (self.x, self.y)

    def reset(self):
        self.x = self.screen.get_width()+25


class Bomb(pygame.sprite.Sprite):
    def __init__(self,posPlane,screen):
        pygame.sprite.Sprite.__init__(self)
        white = 255, 255, 255
        self.screen = screen
        self.x = posPlane[0]
        self.y = posPlane[1]+10
        self.image = pygame.image.load("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.release = False
        self.friction = 0

    def update(self,posPlane):

        if self.release and self.y < 240:
            self.y +=2
            self.x = posPlane[0] + self.friction
            self.friction += .2
            #print(self.friction)
        else:
            #print("plane :" + str(posPlane))
            self.y = posPlane[1] + 10
            self.x = posPlane[0]
            self.friction = 0
            self.release = False

        if self.x < -25:
            self.reset()
        self.rect.center = (self.x, self.y)

    def reset(self):
        self.x = self.screen.get_width() + 25


