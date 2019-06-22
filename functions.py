import pygame
from constants import *
pygame.init()
pygame.font.init()
fontSize = 20

screen = pygame.display.set_mode(dimensions)
defaultFont = pygame.font.SysFont('Verdana', fontSize)

# ==================== FUNCTIONS ==================== #

def count_characters_string(string):
    count = 0
    for characters in string:
        count += 1
    return count

def draw_rectangle(rect_pos_x, rect_pos_y, background_color, width, height):
    pygame.draw.rect(screen, background_color, [rect_pos_x, rect_pos_y, width, height])

def draw_text_with_rectangle(rect_pos_x, rect_pos_y, background_color, text):
    width = count_characters_string(text) * 12
    height = fontSize * 1.5

    draw_rectangle(rect_pos_x, rect_pos_y, black, width, height)
    draw_rectangle(rect_pos_x + 2, rect_pos_y + 2, background_color, width - 4, height - 4)
    text_surface = defaultFont.render(text, False, (0, 0, 0))
    screen.blit(text_surface, (rect_pos_x, rect_pos_y))

    return text_surface.get_rect()

def point_inside_rect():
    inside = False
    return inside