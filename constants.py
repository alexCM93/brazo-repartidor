"""
Global constants
"""
import pygame
pygame.init()
framesPerSecond = 60
# Game clock
clock = pygame.time.Clock()

# define colors
lightgrey = (150, 150, 150)
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# define part data list
colors = [grey, white, green, red]
pesos = [5, 10, 15, 20]

# define program states
menuState = 0
mainState = 1
resultsState = 2
states = [menuState, mainState, resultsState]

# define screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)

# define initial part position
initialX = 155
initialY = -70

# define default font
fontSize = 20
defaultFont = pygame.font.SysFont('Verdana', fontSize)

# define image path and name
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
