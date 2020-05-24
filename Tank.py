# this is a trying to implement the old game Tank in python
import pygame
# init pygame
pygame.init()

print("hello in Tank Game")
#constant
black = 0, 0, 0
# create the main window
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bishop' Tank")

#create the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)



# pygame main event loop
run = True
clock = pygame.time.Clock()

while run:
    # set frame number per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # we quit the game

    screen.blit(background,(0,0))
    pygame.display.flip()

##########################
pygame.quit()