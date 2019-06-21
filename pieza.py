import pygame
class pieza(pygame.Surface):
    def __init__(self, parent, xpos, ypos, width, height):
      super(myRect, self).__init__(width, height)
      self.xpos = xpos
      self.ypos = ypos
      self.parent = parent

    def update(self, parent):
      parent.blit(self, (self.xpos, self.ypos))

    def rotate(self, angle):
        rotatedRect = pygame.transform.rotate(rect, self.rotation)
        screen.blit(rotatedRect)