from constants import *


def text(screen, X, Y, text, render=True):
    defaultFont = pygame.font.SysFont('Verdana', 17)
    Text = defaultFont.render(str(text), True, black)
    TextRect = Text.get_rect()
    TextRect.center = (X, Y)
    if render:
        screen.blit(Text, TextRect)
    return TextRect


class Drop_Down:
    def __init__(self, pos, options, surface, index=0):
        self.pos = pos
        self.options = options
        self.index = index
        self.rect = pygame.Rect(*pos, 85, 30 * len(options))
        self.lines = []
        self.mode = 0
        self.surface = surface
        self.text = text
        self.rects = []

        for x in range(len(options)):
            self.lines.append(((pos[0], pos[1] + (x * 30)), (self.rect.right, pos[1] + (x * 30))))
            self.rects.append(pygame.Rect(pos[0], pos[1] + (30 * x), 85, 30))

    def draw(self):
        if self.mode == 1:
            pygame.draw.rect(self.surface, white, self.rect)
            pygame.draw.rect(self.surface, lightgrey, self.rects[self.index])
            for line in self.lines:
                pygame.draw.line(self.surface, black, line[0], line[1])
            for text in self.options:
                self.text(self.surface, *self.rects[self.options.index(text)].center, text)
        if self.mode == 0:
            pygame.draw.rect(self.surface, lightgrey, self.rects[0])
            self.text(self.surface, *self.rects[0].center, self.options[self.index])

    def get_status(self):
        return self.options[self.index]

    def set_status(self, op):
        self.index = self.options.index(op)

    def events(self, event):
        mouse_rect = pygame.Rect(*pygame.mouse.get_pos(), 2, 2)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.mode == 0:
                if self.rects[0].contains(mouse_rect):
                    self.mode = 1
            elif self.mode == 1:
                for rect in self.rects:
                    if rect.contains(mouse_rect):
                        self.mode = 0
                        self.index = self.rects.index(rect)
