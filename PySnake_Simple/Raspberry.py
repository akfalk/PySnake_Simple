import random
import pygame
from pygame.locals import *

class Raspberry():
    """The raspberry that the snake must eat."""

    def __init__(self, colour):
        """Creates a new instance of Raspberry"""
        self.position = [300, 300]
        self.spawned = 1
        self.colour = colour

    def spawn(self):
        """Spawns a new position for the Raspberry"""
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        self.position = [int(x*20),int(y*20)]
        self.spawned = 1

    def draw(self, playSurface):
       """Draws the raspberry"""
       pygame.draw.rect(playSurface,self.colour,Rect(self.position[0], self.position[1], 20, 20))

# test
"""
raspberry = Raspberry()
print raspberry.position
print raspberry.spawned
raspberry.spawn()
print raspberry.position
print raspberry.spawned
"""



