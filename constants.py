"""
Global constants
"""
import pygame
framesPerSecond = 60

# Colors
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# part Data
colors = [grey, white, green, red]
pesos = [5, 10, 15, 20]
forms = [0, 1, 2, 3]

# States
menuState = 0
mainState = 1
resultsState = 2
states = [menuState, mainState, resultsState]

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

# Initial position
initialX = 155
initialY = -70
# Initial speed
initialSpeed_X = 0
initialSpeed_Y = 5

fontSize = 20

# Images
menuBackground = pygame.image.load('images/menu.png')
mainBackground = pygame.image.load('images/main.png')
resultsBackground = pygame.image.load('images/results.png')
brazo1 = pygame.image.load('images/brazo1.png')
brazo2 = pygame.image.load('images/brazo2.png')
cover = pygame.image.load('images/cover.png')
arm0 = pygame.image.load('images/0.png')
arm1 = pygame.image.load('images/1.png')
arm2 = pygame.image.load('images/2.png')
arm3 = pygame.image.load('images/3.png')
arm4 = pygame.image.load('images/4.png')
