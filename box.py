import pygame as pg

class Box:
    def __init__(self, x, y, width, height, color, border_width = -1, border_color = (0, 0, 0)):
        self.surface = pg.Surface((width, height))
        self.surface.fill(color)
        pg.draw.rect(self.surface, border_color, pg.Rect(0, 0, width, height), border_width)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def get_box(self):
        return (self.surface, self.rect)

class Textbox(Box):
    def __init__(self, text, x, y, width, height, color, border_width, border_color):
        Box.__init__(self, x, y, width, height, color, border_width, border_color)
        pg.font.init()
        font = pg.font.SysFont("Verdana", 30)
        self.text = text
        text_surface = font.render("Testing", False, (0, 0, 0))
        self.surface.blit(text_surface, (0, 0))
