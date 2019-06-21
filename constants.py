"""
Global constants
"""
import pygame

# Colors
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
colors = [grey, white, green, red]

# Rectangle width
rectangleWidth = 10
rectangleHeight = 10

framesPerSecond = 60

# States
menuState = 0
mainState = 1
resultsState = 2
states = [menuState, mainState, resultsState]

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

#
beltWidth = 500
containerWidth = 300

# Initial position
initialX = 90
initialY = -50

# Images
menuBackground = pygame.image.load('images/menu.png')
mainBackground = pygame.image.load('images/main.png')
resultsBackground = pygame.image.load('images/results.png')
