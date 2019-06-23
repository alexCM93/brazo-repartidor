from constants import *
import random
pygame.init()
dimensions = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(dimensions)
class Part:
    def __init__(self, menu_pos, init_pos, init_speed, current_pos,
                 current_speed, partColor = grey, partPeso = 10, partForm = 1):
        self.init_pos = init_pos
        self.menu_pos = menu_pos
        self.init_speed = init_speed
        self.current_pos = current_pos
        self.current_speed = current_speed
        self.partColor = partColor
        self.partPeso = partPeso
        self.partForm = partForm
    def drawMenu(self):
        pygame.draw.rect(screen, black, [self.menu_pos[0], self.menu_pos[1], 50, 50])
        pygame.draw.rect(screen, self.partColor, [self.menu_pos[0] + rectangleWidth, self.menu_pos[1] + rectangleHeight, 30, 30])
    #def drawMain(self):
    #def move(self):
    def setData(self):
        self.partColor = random.choice(colors)
        self.partPeso = random.choice(pesos)
        self.partForm = random.choice(forms)
    def getData(self):
        return (self.partColor, self.partPeso, self.partForm)


