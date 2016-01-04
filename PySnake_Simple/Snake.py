import pygame
from pygame.locals import *

class Snake():
    "Contains the snake"

    def __init__(self, colour, playerInput):
        self.position = [100,100]
        self.segments = [[100,100],[80,100],[60,100]]
        self.direction = 'right'
        self.colour = colour
        self.playerInput = playerInput
        self.life = 3

    def getDirection(self, eventList):
        changeDirection = self.direction
        for event in eventList:
            if event.type == KEYDOWN:
                if event.key == self.playerInput['right']:
                    changeDirection = 'right'
                if event.key == self.playerInput['left']:
                    changeDirection = 'left'
                if event.key == self.playerInput['up']:
                    changeDirection = 'up'
                if event.key == self.playerInput['down']:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        if changeDirection == 'right' and not self.direction == 'left':
            self.direction = changeDirection
        if changeDirection == 'left' and not self.direction == 'right':
            self.direction = changeDirection
        if changeDirection == 'up' and not self.direction == 'down':
            self.direction = changeDirection
        if changeDirection == 'down' and not self.direction == 'up':
            self.direction = changeDirection

    def move(self):
        if self.direction == 'right':
            self.position[0] += 20
        if self.direction == 'left':
            self.position[0] -= 20
        if self.direction == 'up':
            self.position[1] -= 20
        if self.direction == 'down':
            self.position[1] += 20
        self.segments.insert(0,list(self.position)) #The new snakehead

    def checkPosition(self):
        gameOver = False
        # check if outside of x-borders
        if self.position[0] > 620 or self.position[0] < 0:
            gameOver = True
  
        # check if outside of y-borders
        if self.position[1] > 460 or self.position[1] < 0:
            gameOver = True

        # check if snake crosses itself
        if self.position in self.segments[1:]:
            gameOver = True

        return gameOver

    def checkIntersect(self, snakeList):
        for snake in snakeList:
            if self != snake:
                if self.position in snake.segments[1:]:
                    self.life -= 1
                    print snake, "looses one life"
            
    def draw(self, playSurface):
        for position in self.segments:
            pygame.draw.rect(playSurface,self.colour,Rect(position[0], position[1], 20, 20))
            #pygame.draw.circle(playSurface,self.colour, position, 10, 0)