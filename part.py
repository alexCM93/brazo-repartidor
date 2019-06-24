from constants import *
import random

pygame.init()


# class Part, controls part object movement, position and size

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

    def drawMenu(self):  # draws all parts on the menu screen
        pygame.draw.rect(screen, black, [self.menu_pos[0], self.menu_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + self.partPeso,
                                                  self.menu_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])

    def move(self, n):  # moves the initial position of part so they don't draw over eachother
        self.menu_pos = (125 + 69 * n, 498)

    def moveMain(self, n):  # moves parts vertically on main screen so they don't draw over eachother
        if self.current_pos == self.init_pos:
            self.current_pos = [156, -120 * n]

    def setData(self):  # assigns a random color and weight to every part object
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)

    def drawMain(self):

        # change direction when part is at horizontal belt
        if self.current_pos[1] > 350 and self.current_pos[0] == 156:
            self.current_speed[1] = 0
            self.current_speed[0] = 2

        # change direction depending on part color
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

        # restore horizontal movevent when part is in container
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

        # move the part according to it's speed
        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw the part
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                                  self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])

        # draw the arm
        if self.current_pos[0] > 476 and self.current_pos[0] < 500:
            if self.partColor == white:
                arm = arm1
                screen.blit(arm, (353, 240))
            if self.partColor == green:
                arm = arm2
                screen.blit(arm, (353, 240))
            if self.partColor == red:
                arm = arm3
                screen.blit(arm, (353, 240))
            if self.partColor == grey:
                arm = arm4
                screen.blit(arm, (353, 240))
        else:
            screen.blit(arm0, (353, 240))

    def drawMainFast(self, n):

        if self.current_pos[1] > 350 and self.current_pos[0] == 156:
            self.current_speed[1] = 0
            self.current_speed[0] = 2 * n

        speeda = -3 * n
        speedb = -0.9 * n
        speedc = 0.9 * n
        speedd = 3 * n
        if self.current_pos[0] == 476:
            if self.partColor == white:
                self.current_speed[1] += speeda
                self.current_speed[0] = 1 * n
            if self.partColor == green:
                self.current_speed[1] += speedb
            if self.partColor == red:
                self.current_speed[1] += speedc
            if self.partColor == grey:
                self.current_speed[1] += speedd
                self.current_speed[0] = 1 * n

            # Item is in container

        if self.current_pos[0] == 562:
            if self.partColor == white:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
            if self.partColor == grey:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
        if self.current_pos[0] >= 665:
            if self.partColor == green:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
            if self.partColor == red:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n

        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw rectangles
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                                  self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])
        if self.current_pos[0] > 476 and self.current_pos[0] < 525:
            if self.partColor == white:
                arm = arm1
                screen.blit(arm, (353, 240))
            if self.partColor == green:
                arm = arm2
                screen.blit(arm, (353, 240))
            if self.partColor == red:
                arm = arm3
                screen.blit(arm, (353, 240))
            if self.partColor == grey:
                arm = arm4
                screen.blit(arm, (353, 240))
        else:
            screen.blit(arm0, (353, 240))

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
        if self.current_pos[0] > 476 and self.current_pos[0] < 500:
            if self.partPeso == 5:
                arm = arm1
                screen.blit(arm, (353, 240))
            if self.partPeso == 10:
                arm = arm2
                screen.blit(arm, (353, 240))
            if self.partPeso == 15:
                arm = arm3
                screen.blit(arm, (353, 240))
            if self.partPeso == 20:
                arm = arm4
                screen.blit(arm, (353, 240))
        else:
            screen.blit(arm0, (353, 240))

    def drawMainPesoFast(self, n):

        if self.current_pos[1] > 350 and self.current_pos[0] == 156:
            self.current_speed[1] = 0 * n
            self.current_speed[0] = 2 * n

        speeda = -3 * n
        speedb = -0.9 * n
        speedc = 0.9 * n
        speedd = 3 * n
        arm = cover

        if self.current_pos[0] == 476:
            if self.partPeso == 5:
                self.current_speed[1] += speeda
                self.current_speed[0] = 1 * n
            if self.partPeso == 10:
                self.current_speed[1] += speedb
            if self.partPeso == 15:
                self.current_speed[1] += speedc
            if self.partPeso == 20:
                self.current_speed[1] += speedd
                self.current_speed[0] = 1 * n

            # Item is in container

        if self.current_pos[0] == 562:
            if self.partPeso == 5:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
            if self.partPeso == 20:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
        if self.current_pos[0] >= 665:
            if self.partPeso == 10:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n
            if self.partPeso == 15:
                self.current_speed[1] = 0
                self.current_speed[0] = 2 * n

        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw rectangles
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                                  self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])
        if self.current_pos[0] > 476 and self.current_pos[0] < 525:
            if self.partPeso == 5:
                arm = arm1
                screen.blit(arm, (353, 240))
            if self.partPeso == 10:
                arm = arm2
                screen.blit(arm, (353, 240))
            if self.partPeso == 15:
                arm = arm3
                screen.blit(arm, (353, 240))
            if self.partPeso == 20:
                arm = arm4
                screen.blit(arm, (353, 240))
        else:
            screen.blit(arm0, (353, 240))

    def drawResults(self, y):  # draw parts in results screen
        pygame.draw.rect(screen, black, [self.menu_pos[0], y, 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + self.partPeso,
                                                  y + self.partPeso, 50 - self.partPeso * 2,
                                                  50 - self.partPeso * 2])
