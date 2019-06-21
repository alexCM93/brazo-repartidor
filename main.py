import pygame
from constants import *
import random

pygame.init()

# Screen data
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Brazo repartidor")

# Main loop flag control
run = True

# Game clock
clock = pygame.time.Clock()

# State variable
state = states[1]

# Current speed and position
currentSpeed_X = 0
currentSpeed_Y = 5
pos_x = initialX
pos_y = initialY

color = random.choice(colors)
remainingItems = 2

background = mainBackground

# ==================== MAIN LOOP ==================== #

while run:
    # Define FPS
    clock.tick(framesPerSecond)

    # Empty screen
    screen.fill(black)

    # End program if user quits game
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    # State is menu
    if state == states[0]:
        background = menuBackground

    # State is main
    if state == states[1]:
        background = mainBackground

        # == Move rectangle depending on condition == #

        if pos_y > 340 and pos_x == 90:
            currentSpeed_Y = 0
            currentSpeed_X = 5

        # Item is inside distributor
        if pos_x > beltWidth:
            if color == white:
                currentSpeed_Y = -4
            if color == green:
                currentSpeed_Y = 4
            if color == red:
                currentSpeed_Y = 2
            if color == grey:
                currentSpeed_Y = -2

        # Item is in container
        if pos_x > beltWidth + containerWidth:
            currentSpeed_Y = 0

            # Item is out of screen
        if pos_x > SCREEN_WIDTH:
            currentSpeed_Y = 5
            currentSpeed_X = 0
            pos_x = initialX
            pos_y = initialY
            color = random.choice(colors)
            remainingItems = remainingItems - 1

        pos_x += currentSpeed_X
        pos_y += currentSpeed_Y

        # Change state to results when empty list
        if remainingItems == 0:
            state = states[2]

    # State is results
    if state == states[2]:
        background = resultsBackground

    screen.blit(background, (0, 0))

    # Draw background
    screen.blit(background, (0, 0))

    # Draw rectangles
    pygame.draw.rect(screen, black, [pos_x, pos_y, 50, 50])
    pygame.draw.rect(screen, color, [pos_x + rectangleWidth, pos_y + rectangleHeight, 30, 30])

    # Update screen
    pygame.display.flip()

# Close pygame library instance
pygame.quit()
