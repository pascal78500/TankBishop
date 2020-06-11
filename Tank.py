# this is a trying to implement the old game Tank in python
import pygame
import Stank
import Splane
import random

# init pygame
pygame.init()

print("hello in Tank Game")
#constant
black = 0, 0, 0
white = 255,255,255
green = 0,200,0
counter = 0
GameOver = False
GroundY = 240 # level where the ground is drawn

# create the main window
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bishop' Tank")

#create the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
myfont = pygame.font.SysFont("Comic Sans MS",30)
Label = myfont.render("Hit Space Bar to release the bomb",1,white)

# pygame main event loop
run = True
clock = pygame.time.Clock()
tank = Stank.Tank(screen)
plane = Splane.Plane(screen)
bomb = Splane.Bomb(plane.rect.center,screen)
score = Stank.ScoreBoard()
explosion = Stank.Explosion(tank.rect.center)

TankSprite = pygame.sprite.Group(tank)
PlaneSprite = pygame.sprite.Group(plane)
BombSprite = pygame.sprite.Group(bomb)
ScoreSprite = pygame.sprite.Group(score)
ExplosionSprite = pygame.sprite.Group(explosion)

while run:
    # set frame number per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # we quit the game
        if event.type == pygame.KEYDOWN: # check if a key i pressed
            if event.key == pygame.K_SPACE and not GameOver:
                bomb.release = True
            if event.key == pygame.K_r and GameOver: # reset the game
                GameOver = False
                score.TanksHits = 0
                score.TimeLeft = 60
                screen.blit(background, (0, 0))
            if event.key == pygame.K_q: # exit the game with q pressed on qwerty, a on azerty
                run = False

    # test collision between bomb and tank
    if bomb.rect.colliderect(tank.rect):
        bomb.release = False
        score.TanksHits += 1
        tank.hitted = True # show explosion in update method instead of tank
        explosion.SrcPoint = (tank.x-200,235) # replace value by variable !!!
        tank.reset()


    if counter >= 60: # implement a pseudo timer around 1 sec.
        counter = 0
        score.TimeLeft -= 1

    if score.TimeLeft == 0:
        # game over
        GameOver = True
        counter = 0
        OverLabel = myfont.render("Game Over",1,white)
        screen.blit(OverLabel,(250,100))

    pygame.draw.rect(screen,white,(0,GroundY,width,30))
    pygame.draw.line(screen, green, [0, GroundY], [width, GroundY], 5) # the thin green line on top of white rectangle
    screen.blit(Label,(50,330))

    if tank.hitted:

        for pos in range(100):
            TankSprite.clear(screen, background)
            PlaneSprite.clear(screen, background)
            BombSprite.clear(screen, background)
            ScoreSprite.clear(screen, background)
            ExplosionSprite.clear(screen, background)

            explosion.pos = pos
            ExplosionSprite.update()
            PlaneSprite.update()
            BombSprite.update(plane.rect.center)
            ScoreSprite.update()

            ExplosionSprite.draw(screen)
            PlaneSprite.draw(screen)
            BombSprite.draw(screen)
            ScoreSprite.draw(screen)

            pygame.display.flip()
        tank.hitted = False

    else:
        TankSprite.clear(screen,background)
        PlaneSprite.clear(screen,background)
        BombSprite.clear(screen,background)
        ScoreSprite.clear(screen,background)
        ExplosionSprite.clear(screen,background)

        TankSprite.update()
        PlaneSprite.update()
        BombSprite.update(plane.rect.center)
        ScoreSprite.update()

        TankSprite.draw(screen)
        PlaneSprite.draw(screen)
        BombSprite.draw(screen)
        ScoreSprite.draw(screen)

        pygame.display.flip()

    counter += 1

##########################
pygame.quit()