from constants import *


def text(screen, X, Y, text, render=True):  # draws centered text only if render=true, when dropdown active
    defaultFont = pygame.font.SysFont('Verdana', 17)
    Text = defaultFont.render(str(text), True, black)
    TextRect = Text.get_rect()
    TextRect.center = (X, Y)
    if render:
        screen.blit(Text, TextRect)
    return TextRect


class Drop_Down:  # draws a selectable dropdown menu
    def __init__(self, pos, options, surface, index=0):
        self.pos = pos
        self.options = options
        self.index = index
        self.rect = pygame.Rect(*pos, 85, 30 * len(options))
        self.lines = []
        self.open = 0
        self.surface = surface
        self.text = text
        self.rects = []
        for x in range(len(options)):  # draws lines separating the options
            self.lines.append(((pos[0], pos[1] + (x * 30)), (self.rect.right, pos[1] + (x * 30))))
            self.rects.append(pygame.Rect(pos[0], pos[1] + (30 * x), 85, 30))

    def draw(self):
        if self.open == 0:  # if menu is not open draw only first option
            pygame.draw.rect(self.surface, lightgrey, self.rects[0])
            self.text(self.surface, *self.rects[0].center, self.options[self.index])
        if self.open == 1:  # if menu is open draw all options
            pygame.draw.rect(self.surface, white, self.rect)
            pygame.draw.rect(self.surface, lightgrey, self.rects[self.index])
            for line in self.lines:
                pygame.draw.line(self.surface, black, line[0], line[1])
            for text in self.options:
                self.text(self.surface, *self.rects[self.options.index(text)].center, text)

    def get_status(self):
        return self.options[self.index]

    def set_status(self, op):
        self.index = self.options.index(op)

    def events(self, event):  # detects clicks on the dropdown
        mouse_rect = pygame.Rect(*pygame.mouse.get_pos(), 2, 2)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.open == 0:  # opens dropdown
                if self.rects[0].contains(mouse_rect):
                    self.open = 1
            elif self.open == 1:  # selects option and closes dropdown
                for rect in self.rects:
                    if rect.contains(mouse_rect):
                        self.open = 0
                        self.index = self.rects.index(rect)
