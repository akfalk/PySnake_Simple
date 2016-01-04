# Raspberry Snake was originally written by Gareth Halfacree for the Raspberry Pi User Guide.
# The original code is located in the Download section of the book's hompage:
# http://wiley.com/go/raspberrypiuserguide
# This version is grossly modified by akfalk towards an object-oriented design.
# This version is a two-player version

from Raspberry import Raspberry
from Snake import Snake
import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raspberry Snake')

redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

speed = 3

raspberry = Raspberry(redColour)

playerInput_1 = {'right':K_RIGHT, 'left':K_LEFT, 'up':K_UP, 'down':K_DOWN}
playerInput_2 = {'right':ord('d'), 'left':ord('a'), 'up':ord('w'), 'down':ord('s')}
snake_1 = Snake(whiteColour, playerInput_1)
snake_2 = Snake(greyColour, playerInput_2)

snakeList = [snake_1, snake_2]

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def listenQuit(eventList):
    for event in eventList:
        if event.type == QUIT:
            pygame.quit()

while True:
    eventList = pygame.event.get()
    listenQuit(eventList)
    
    for snake in snakeList: 
        snake.getDirection(eventList)
        snake.move()

        if snake.checkPosition():
            gameOver()

        snake.checkIntersect(snakeList)

        if snake.position == raspberry.position:
            # snake eats raspberry, spawn a new.
            raspberry.spawn()
            speed += 0.5
        else:
            # remove the tail - a new head has already been added - the snake will only grow longer when it takes a raspberry
            snake.segments.pop() #"pop" without an argument removes the last item of the list

    #put everything in position for redrawing...
    #...first the backdrop
    playSurface.fill(blackColour)

    # ...then draw snake
    for snake in snakeList:
        snake.draw(playSurface)

    # ...then draw raspberry
    raspberry.draw(playSurface)

    # ...finally activte the update of the screen
    pygame.display.flip()

    # advance
    fpsClock.tick(speed)
