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
        self.init_speed = [0, 5]
        self.current_pos = [155, -70]
        self.current_speed = [0, 5]
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)
    def drawMenu(self):
        pygame.draw.rect(screen, black, [self.menu_pos[0], self.menu_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + self.partPeso,
                                                  self.menu_pos[1] + self.partPeso, 50 - self.partPeso * 2, 50 - self.partPeso * 2])
    def move(self, n):
        self.menu_pos = (125 + 69 * n, 498)

    def moveMain(self, n):
        if self.current_pos == self.init_pos:
            self.current_pos = [155, -50 * n]
    def setData(self):
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)
    def getData(self):
        return (self.partColor, self.partPeso, self.partForm)
    def drawMain(self):


        if self.current_pos[1] > 340 and self.current_pos[0] == 155:
            self.current_speed[1] = 0
            self.current_speed[0] = 5

        speeda = -4
        speedb = 4
        speedc = 2
        speedd = -2
        if self.current_pos[0] == 500:
            if self.partColor == white:
                self.current_speed[1] += speeda
            if self.partColor == green:
                self.current_speed[1] += speedb
            if self.partColor == red:
                self.current_speed[1] += speedc
            if self.partColor == grey:
                self.current_speed[1] += speedd

            # Item is in container
        if self.current_pos[0] > 800:
            self.current_speed[1] = 0

            # Item is out of screen
        '''    
        if self.current_pos[0] > 1000:
            currentSpeed_Y = 5
            currentSpeed_X = 0
            pos_x = initialX
            pos_y = initialY
            color = random.choice(colors)
            remainingItems = remainingItems - 1
        '''
        self.current_pos[0] += self.current_speed[0]
        self.current_pos[1] += self.current_speed[1]

        # Draw rectangles
        pygame.draw.rect(screen, black, [self.current_pos[0], self.current_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.current_pos[0] + self.partPeso,
                                              self.current_pos[1] + self.partPeso, 50 - self.partPeso * 2,
                                              50 - self.partPeso * 2])




