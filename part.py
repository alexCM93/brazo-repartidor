from constants import *
import random

pygame.init()
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)


class Part(object):
    def __init__(self, name):
        self.name = name
        self.menu_pos = [125, 498]
        self.init_pos = [155, -70]
        self.init_speed = [0, 2]
        self.current_pos = [155, -70]
        self.current_speed = [0, 2]
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)

    def drawMenu(self):
        pygame.draw.rect(screen, black, [self.menu_pos[0], self.menu_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + self.partPeso,
                                                  self.menu_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])

    def move(self, n):
        self.menu_pos = (125 + 69 * n, 498)

    def moveMain(self, n):
        if self.current_pos == self.init_pos:
            self.current_pos = [156, -120 * n]

    def setData(self):
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)

    def getData(self):
        return (self.partColor, self.partPeso, self.partForm)

    def drawMain(self):

        if self.current_pos[1] > 350 and self.current_pos[0] == 156:
            self.current_speed[1] = 0
            self.current_speed[0] = 2

        speeda = -3
        speedb = -0.9
        speedc = 0.9
        speedd = 3
        if self.current_pos[0] == 476:
            if self.partColor == white:
                self.current_speed[1] += speeda
                self.current_speed[0] = 1
            if self.partColor == green:
                self.current_speed[1] += speedb
            if self.partColor == red:
                self.current_speed[1] += speedc
            if self.partColor == grey:
                self.current_speed[1] += speedd
                self.current_speed[0] = 1

            # Item is in container

        if self.current_pos[0] == 562:
            if self.partColor == white:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
            if self.partColor == grey:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
        if self.current_pos[0] >= 665:
            if self.partColor == green:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
            if self.partColor == red:
                self.current_speed[1] = 0
                self.current_speed[0] = 2

        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw rectangles
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                                  self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])

    def drawMainPeso(self):

        if self.current_pos[1] > 350 and self.current_pos[0] == 156:
            self.current_speed[1] = 0
            self.current_speed[0] = 2

        speeda = -3
        speedb = -0.9
        speedc = 0.9
        speedd = 3
        if self.current_pos[0] == 476:
            if self.partPeso == 5:
                self.current_speed[1] += speeda
                self.current_speed[0] = 1
            if self.partPeso == 10:
                self.current_speed[1] += speedb
            if self.partPeso == 15:
                self.current_speed[1] += speedc
            if self.partPeso == 20:
                self.current_speed[1] += speedd
                self.current_speed[0] = 1

            # Item is in container

        if self.current_pos[0] == 562:
            if self.partPeso == 5:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
            if self.partPeso == 20:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
        if self.current_pos[0] >= 665:
            if self.partPeso == 10:
                self.current_speed[1] = 0
                self.current_speed[0] = 2
            if self.partPeso == 15:
                self.current_speed[1] = 0
                self.current_speed[0] = 2

        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw rectangles
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                                  self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])

    def drawResults(self, y):
        pygame.draw.rect(screen, black, [self.menu_pos[0], y, 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + self.partPeso,
                                                  y + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])
