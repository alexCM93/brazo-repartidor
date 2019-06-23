import random
from menu import *
from part import *

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
remainingItems = 3
greyGroup = 0
whiteGroup = 0
greenGroup = 0
redGroup = 0
peso1Group = 0
peso2Group = 0
peso3Group = 0
peso4Group = 0

# menu initial data
repartoDropDown = Drop_Down((435, 250), ["Por color", "Por peso"], screen, color2=gray(100))
brazoDropDown = Drop_Down((572, 295), list(range(1, 3, 1)), screen, color2=gray(100))
repartoDropDown.set_status("Por color")
brazoDropDown.set_status(1)
tipoReparto = repartoDropDown.get_status()

# creating parts
numberOfParts = 10
allparts = []


def randomParts(n, list):
    for i in range(0, n):
        list.append(Part(i))
    return (list)


randomParts(numberOfParts, allparts)


# ==================== FUNCTIONS ==================== #

def draw_rectangle(rect_pos_x, rect_pos_y, background_color, width, height):
    pygame.draw.rect(screen, background_color, [rect_pos_x, rect_pos_y, width, height])


def draw_text_with_rectangle(rect_pos_x, rect_pos_y, background_color, text, width_space):
    width = len(text) * width_space
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
        # print(event)

    # State is menu
    if state == states[0]:
        # draw menu and menu options
        greyGroup = 0
        whiteGroup = 0
        greenGroup = 0
        redGroup = 0
        peso1Group = 0
        peso2Group = 0
        peso3Group = 0
        peso4Group = 0
        for i in range(0, numberOfParts):
            if allparts[i].partColor == white:
                peso1Group += 1
            if allparts[i].partColor == green:
                peso2Group += 1
            if allparts[i].partColor == red:
                peso3Group += 1
            if allparts[i].partColor == grey:
                peso4Group += 1
        for i in range(0, numberOfParts):
            if allparts[i].partColor == white:
                greyGroup += 1
            if allparts[i].partColor == green:
                whiteGroup += 1
            if allparts[i].partColor == red:
                greenGroup += 1
            if allparts[i].partColor == grey:
                redGroup += 1
        background = menuBackground
        repartoDropDown.draw()
        brazoDropDown.draw()
        menuDist = 0
        for i in range(0, numberOfParts):
            allparts[i].move(menuDist)
            allparts[i].drawMenu()
            menuDist += 1

        if brazoDropDown.get_status() == 1:
            screen.blit(brazo1, (693, 200))
            draw_text_with_rectangle(660, 420, grey, 'Brazo Mecánico genérico', 12)
        if brazoDropDown.get_status() == 2:
            screen.blit(brazo2, (693, 200))
            draw_text_with_rectangle(660, 420, grey, 'Brazo Mecánico Premium', 12)
            draw_text_with_rectangle(660, 455, grey, 'Doble velocidad', 12)
        crear_rect = pygame.draw.rect(screen, green, pygame.Rect(480, 340, 90, 30))
        crear = draw_text_with_rectangle(480, 340, grey, 'CREAR', 18)

        # check menu option changes and ENTER key presses
        for event in events:
            mouse_rect = pygame.Rect((*pygame.mouse.get_pos(), 1, 1))
            repartoDropDown.events(event)
            brazoDropDown.events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = states[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crear_rect.collidepoint(event.pos):
                    allparts = []
                    randomParts(numberOfParts, allparts)

    # State is main
    if state == states[1]:
        background = mainBackground
        tipoReparto = repartoDropDown.get_status()
        # == Move rectangle depending on condition == #
        mainDist = 0
        for i in range(0, numberOfParts):
            allparts[i].moveMain(mainDist)
            if tipoReparto == "Por color":
                allparts[i].drawMain()
            if tipoReparto == "Por peso":
                allparts[i].drawMainPeso()
            mainDist += 1
        screen.blit(cover, (0, 0))

        rec_resultados = pygame.draw.rect(screen, green, pygame.Rect(100, 600, 155, 30))
        resultados = draw_text_with_rectangle(100, 600, white, 'RESULTADOS', 16)

        # check menu option changes and ENTER key presses
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec_resultados.collidepoint(event.pos):
                    state = states[2]

    # State is results
    if state == states[2]:
        rec_reset = pygame.draw.rect(screen, green, pygame.Rect(839, 160, 80, 30))
        background = resultsBackground
        if tipoReparto == "Por color":
            run_button2 = draw_text_with_rectangle(75, 285, grey, str(greyGroup), 30)
            run_button3 = draw_text_with_rectangle(75, 370, grey, str(whiteGroup), 30)
            run_button4 = draw_text_with_rectangle(75, 455, grey, str(greenGroup), 30)
            run_button5 = draw_text_with_rectangle(75, 540, grey, str(redGroup), 30)
            whiteDist = 0
            greenDist = 0
            redDist = 0
            greyDist = 0
            for i in range(0, numberOfParts):
                if allparts[i].partColor == white:
                    allparts[i].move(whiteDist)
                    allparts[i].drawResults(275)
                    whiteDist += 1
                if allparts[i].partColor == green:
                    allparts[i].move(greenDist)
                    allparts[i].drawResults(360)
                    greenDist += 1
                if allparts[i].partColor == red:
                    allparts[i].move(redDist)
                    allparts[i].drawResults(445)
                    redDist += 1
                if allparts[i].partColor == grey:
                    allparts[i].move(greyDist)
                    allparts[i].drawResults(530)
                    greyDist += 1
        if tipoReparto == "Por peso":
            run_button2 = draw_text_with_rectangle(75, 285, grey, str(peso1Group), 30)
            run_button3 = draw_text_with_rectangle(75, 370, grey, str(peso2Group), 30)
            run_button4 = draw_text_with_rectangle(75, 455, grey, str(peso3Group), 30)
            run_button5 = draw_text_with_rectangle(75, 540, grey, str(peso4Group), 30)
            peso1Dist = 0
            peso2Dist = 0
            peso3Dist = 0
            peso4Dist = 0
            for i in range(0, numberOfParts):
                if allparts[i].partPeso == 5:
                    allparts[i].move(peso1Dist)
                    allparts[i].drawResults(275)
                    peso1Dist += 1
                if allparts[i].partPeso == 10:
                    allparts[i].move(peso2Dist)
                    allparts[i].drawResults(360)
                    peso2Dist += 1
                if allparts[i].partPeso == 15:
                    allparts[i].move(peso3Dist)
                    allparts[i].drawResults(445)
                    peso3Dist += 1
                if allparts[i].partPeso == 20:
                    allparts[i].move(peso4Dist)
                    allparts[i].drawResults(530)
                    peso4Dist += 1


        # check menu option changes and ENTER key presses

        reset = draw_text_with_rectangle(839, 160, white, 'RESET', 16)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec_reset.collidepoint(event.pos):
                    state = states[0]
                    allparts = []
                    randomParts(numberOfParts, allparts)
    # Update screen
    pygame.display.flip()

# Close pygame library
pygame.quit()
