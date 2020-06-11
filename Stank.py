# define the class tank
import pygame
import random
import math
import time

class Tank(pygame.sprite.Sprite):
    """ define the Tank class to manage the sprite"""
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank.png")
        self.screen = screen
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 227
        self.rect.center = (self.x,self.y)
        self.vx_range = (1, 0, 0.5, 2, -0.5,-3,-1,0.7,-0.7,0.2,-0.2)
        self.vx = self.vx_range[0]
        self.hitted = False

    def update(self):
        """update method to update the drawing of the tank"""
        self.x +=self.vx
        if self.x > self.screen.get_width()+27 and self.vx > 0:
            self.x = -7
        elif self.x < 0 and self.vx < 0:
            self.x = self.screen.get_width() + 27
        self.rect.center = (self.x, self.y)

    def reset(self):
        """ define new speed after tank hit"""
        self.vx = self.vx_range[random.randrange(11)]

class ScoreBoard(pygame.sprite.Sprite):
    """Class to manage information dashboard"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.TanksHits = 0
        self.TimeLeft = 60
        self.myFont = pygame.font.SysFont("Comic Sans MS", 30)

    def update(self):
        """Updte the scoring information on the board"""
        white = (255,255,255)
        self.Text = "Tanks Hits :%d     Time Left :%d" % (self.TanksHits,self.TimeLeft)
        self.image = self.myFont.render(self.Text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.center = (300,300)


class Explosion(pygame.sprite.Sprite):
    def __init__(self,Srcpoint):
        pygame.sprite.Sprite.__init__(self)
        self.traj = []
        self.traj_len = []
        self.alpha = 0.1
        self.SrcPoint = (200,100)
        self.image = pygame.Surface((400, 100))
        self.image.convert()
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (Srcpoint[0]-200, 235)

        self.largeur, self.hauteur = self.image.get_size()

        self.pos = 0

        while self.alpha < math.pi:
            self.reset()
            self.traj_i = []
            self.trajectory()

            if len(self.traj_i) < 1000:
                self.traj.append(self.traj_i)
            self.alpha += 0.05

    def reset(self):

        self.v = random.uniform(1, 5)
        self.v_x = self.v * math.cos(self.alpha)
        self.v_y = self.v * math.sin(self.alpha)
        self.a_y = -9.81 / 100

    def trajectory(self):

        X_limit = 2000
        t = 0
        Y = self.SrcPoint[1]
        X = self.SrcPoint[0]

        while (int(Y) >= 0 and int(X) < self.largeur and X > 0) and t < X_limit:
            if Y >= 0 and X <= self.largeur:
                X = X + self.v_x
                self.v_y = self.v_y + self.a_y
                Y = Y - self.v_y
                pos = [int(X), int(Y)]
                self.traj_i.append(pos)

            t += 1

        if t < X_limit:
            self.traj_len.append(len(self.traj_i))
        else:
            self.traj_i = []

    def draw_pos(self):
        time.sleep(0.015)  # slow down the animation
        for i in range(len(self.traj)):
            if self.pos < len(self.traj[i]):
                if self.pos < len(self.traj[0]):
                    colorpoint = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
                    pygame.draw.circle(self.image, colorpoint, self.traj[i][self.pos], 1)


    def update(self):
        self.rect.bottomleft= self.SrcPoint
        self.image.fill((0, 0, 0))
        self.draw_pos()