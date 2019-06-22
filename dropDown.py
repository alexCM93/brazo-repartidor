import pygame

pygame.init()


def text(DISPLAYSURF, X, Y, size, color, text1, anchor="topleft", render=True):
    BASICFONT = pygame.font.Font('freesansbold.ttf', size)
    Text = BASICFONT.render(str(text1), True, color)
    TextRect = Text.get_rect()
    exec("TextRect.%s = (X,Y)" % anchor)
    if render:
        DISPLAYSURF.blit(Text, TextRect)
    return TextRect

class Drop_Down:
    def __init__(self, pos, options, surface, color=(255, 255, 255), color2=(150, 150, 150), text_size=17, index=0,
                 width=75, height=30):
        self.pygame = pygame
        self.pos = pos
        self.options = options
        self.index = index
        self.text_size = text_size
        self.height = height
        self.width = width
        self.rect = pygame.Rect(*pos, width, self.height * len(options))
        self.lines = []
        self.mode = 0
        self.surface = surface
        self.text = text
        self.rects = []
        self.color = color
        self.color2 = color2
        for x in range(len(options)):
            self.lines.append(((pos[0], pos[1] + (x * self.height)), (self.rect.right, pos[1] + (x * self.height))))
            self.rects.append(pygame.Rect(pos[0], pos[1] + (height * x), width, height))

    def draw(self):
        if self.mode == 1:
            self.pygame.draw.rect(self.surface, self.color, self.rect)
            self.pygame.draw.rect(self.surface, self.color2, self.rects[self.index])
            for line in self.lines:
                self.pygame.draw.line(self.surface, (0, 0, 0), line[0], line[1])
            for text in self.options:
                self.text(self.surface, *self.rects[self.options.index(text)].center, self.text_size, (0, 0, 0), text,
                          anchor="center")
        if self.mode == 0:
            self.pygame.draw.rect(self.surface, self.color2, self.rects[0])
            self.text(self.surface, *self.rects[0].center, self.text_size, (0, 0, 0), self.options[self.index],
                      anchor="center")

    def get_status(self):
        return self.options[self.index]

    def set_status(self, op):
        self.index = self.options.index(op)

    def events(self, event):
        mouse_rect = self.pygame.Rect(*self.pygame.mouse.get_pos(), 1, 1)
        if event.type == self.pygame.MOUSEBUTTONDOWN:
            if self.mode == 0:
                if self.rects[0].colliderect(mouse_rect):
                    self.mode = 1
            elif self.mode == 1:
                for rect in self.rects:
                    if rect.colliderect(mouse_rect):
                        self.mode = 0
                        self.index = self.rects.index(rect)

def Adv_Fonts(pos, display, size, text, font = "Sans", color = (0, 0, 0),  italic = False, bold = False, AA = True, underline = False, anchor = "center", render = True, shadow = False, shadowDistance = 2):
    rfont = pygame.font.SysFont(font, size)
    rfont.set_italic(italic)
    rfont.set_bold(bold)
    rfont.set_underline(underline)
    Text = rfont.render(str(text), AA, color)
    TextRect = Text.get_rect()
    exec("TextRect.%s = pos" % anchor)
    if shadow:
        font2 = pygame.font.SysFont(font, size)
        font2.set_italic(italic)
        font2.set_bold(bold)
        font2.set_underline(underline)
        Text2 = font2.render(str(text), AA, (0, 0, 0))
        TextRect2 = Text2.get_rect()
        Pos2 = (pos[0] + shadowDistance, pos[1] + shadowDistance)
        exec("TextRect2.%s = Pos2" % anchor)
    if render:
        if shadow:
            display.blit(Text2, TextRect2)
        display.blit(Text, TextRect)
    return (Text, TextRect)

def draw_menu(self):
        self.Display.blit(self.images["MainMenu"], (0, 0))
        self.subDropDown.draw()
        self.minesDropDown.draw()
        self.themeDropDown.draw()

        Adv_Fonts(self.scale((90, 580)),
                  self.Display, self.scaleY(15), "Grid Subdivisions",
                  color=(255, 255, 0), font="freesansbold", bold=True, anchor="topleft")

        Adv_Fonts(self.scale((200, 580)),
                  self.Display, self.scaleY(15), "Mine Density",
                  color=(255, 255, 0), font="freesansbold", bold=True, anchor="topleft")

        Adv_Fonts(self.scale((300 + self.scaleX(75 / 2), 580)),
                  self.Display, self.scaleY(15), "Theme",
                  color=(255, 255, 0), font="freesansbold", bold=True, anchor="midtop")

        Adv_Fonts((self.Display.get_width() // 2, self.Display.get_height() // 2),
                  self.Display, self.scaleY(50), "Press Enter to Continue",
                  color=(255, 255, 0), font="monospace", bold=True)

        Adv_Fonts((self.Display.get_width() // 2, self.Display.get_height() - self.scaleY(100)),
                  self.Display, self.scaleY(20), "Press <R> to regenerate board",
                  color=(255, 255, 0), font="monospace", bold=True)
Display = 1
def gray(v):
    return (v,v,v)
subDropDown = Drop_Down((100, 600), list(range(5, 19)),
        Display, color2 = gray(100))
minesDropDown = Drop_Down((200, 600), list(range(5, 76, 5)),
        Display, color2 = gray(100))
themeDropDown = Drop_Down((300, 600), ["Light", "Dark", "Nacho"],
        Display, color2 = gray(100))
subDropDown.set_status(10)
minesDropDown.set_status(25)
themeDropDown.set_status("Dark")