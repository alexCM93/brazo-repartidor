from constants import *
import random
pygame.init()
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)
class Part(object):
    def __init__(self, name):
        self.name = name
        self.menu_pos = (125, 498)
        self.init_pos = (500, 500)
        self.init_speed = (5, 5)
        self.current_pos = (500, 500)
        self.current_speed = (5, 5)
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)
    def drawMenu(self):
        pygame.draw.rect(screen, black, [self.menu_pos[0], self.menu_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + rectangleWidth, self.menu_pos[1] + rectangleHeight, 30, 30])
    #def drawMain(self):
    def move(self, n ):
        self.menu_pos = (125 + 69 * n, 498)
    def setData(self):
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)
    def getData(self):
        return (self.partColor, self.partPeso, self.partForm)


