from constants import *
import random
from menu import *
pygame.init()
pygame.font.init()

# Screen data
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Brazo repartidor")
defaultFont = pygame.font.SysFont('Verdana', fontSize)

# Game clock
clock = pygame.time.Clock()

# State variable and background
state = states[0]
background = menuBackground

# initial part parameters
currentSpeed_X = 0
currentSpeed_Y = 5
pos_x = initialX
pos_y = initialY
color = random.choice(colors)

# groups
remainingItems = 2
greyGroup = 0
whiteGroup = 0
greenGroup = 0
redGroup = 0

# menu initial data
repartoDropDown = Drop_Down((435, 250), ["Por color", "Por peso", "Por forma"], screen, color2=gray(100))
brazoDropDown = Drop_Down((572, 295), list(range(1, 3, 1)), screen, color2=gray(100))
repartoDropDown.set_status("Por color")
brazoDropDown.set_status(1)

# ==================== FUNCTIONS ==================== #

def draw_rectangle(rect_pos_x, rect_pos_y, background_color, width, height):
    pygame.draw.rect(screen, background_color, [rect_pos_x, rect_pos_y, width, height])

def draw_text_with_rectangle(rect_pos_x, rect_pos_y, background_color, text):
    width = len(text) * 30
    height = fontSize * 1.5

    draw_rectangle(rect_pos_x, rect_pos_y, black, width, height)
    draw_rectangle(rect_pos_x + 2, rect_pos_y + 2, background_color, width - 4, height - 4)
    text_surface = defaultFont.render(text, False, (0, 0, 0))
    screen.blit(text_surface, (rect_pos_x + 7, rect_pos_y))

    return text_surface.get_rect()

# Main loop flag control
run = True

# ==================== MAIN LOOP ==================== #

while run:
    # Define FPS
    clock.tick(framesPerSecond)

    # Empty screen
    screen.fill(black)

    # Draw background
    screen.blit(background, (0, 0))

    # Save events from Pygame
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False
        print(event)
    # State is menu
    if state == states[0]:
        # draw menu and menu options
        background = menuBackground
        repartoDropDown.draw()
        brazoDropDown.draw()

        # check menu option changes and ENTER key presses
        for event in events:
            repartoDropDown.events(event)
            brazoDropDown.events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = states[1]

    # State is main
    if state == states[1]:
        background = mainBackground

        # == Move rectangle depending on condition == #

        if pos_y > 340 and pos_x == 90:
            currentSpeed_Y = 0
            currentSpeed_X = 5

        # Item is inside distributor
        if pos_x == beltWidth:
            if color == white:
                currentSpeed_Y = -4
                whiteGroup = whiteGroup + 1
            if color == green:
                currentSpeed_Y = 4
                greenGroup = greenGroup + 1
            if color == red:
                currentSpeed_Y = 2
                redGroup = redGroup + 1
            if color == grey:
                currentSpeed_Y = -2
                greyGroup = greyGroup + 1

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

        # Draw rectangles
        pygame.draw.rect(screen, black, [pos_x, pos_y, 50, 50])
        pygame.draw.rect(screen, color, [pos_x + rectangleWidth, pos_y + rectangleHeight, 30, 30])

        # Change state to results when empty list
        if remainingItems == 0:
            state = states[2]

    # State is results
    if state == states[2]:
        background = resultsBackground
        run_button2 = draw_text_with_rectangle(211, 323, grey, str(greyGroup))
        run_button3 = draw_text_with_rectangle(415, 323, grey, str(whiteGroup))
        run_button4 = draw_text_with_rectangle(613, 323, grey, str(greenGroup))
        run_button5 = draw_text_with_rectangle(811, 323, grey, str(redGroup))

    # Update screen
    pygame.display.flip()

# Close pygame library
pygame.quit()
