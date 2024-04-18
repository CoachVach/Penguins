from App.Constants.Cells.cells import *
from App.Constants.Cells.interface import *
from App.Interface.Images.image_transformer import cell_img


class CellDrawer:
    def __init__(self, screen):
        self.screen = screen

        self.width = CELL_WIDTH
        self.height = CELL_HEIGHT

        self.empty_img = cell_img(EMPTY_IMG)
        self.rock_img = cell_img(ROCK_IMG)
        self.water_img = cell_img(WATER_IMG)
    
    def draw(self, cell, j, i, x, y):
        if cell == EMPTY:
            self.draw_empty(j, i, x, y)
        elif cell == ROCK:
            self.draw_rock(j, i, x, y)
        elif cell == WATER:
            self.draw_water(j, i, x, y)

    def draw_empty(self, j, i, x, y):
        self.screen.blit(self.empty_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_rock(self, j, i, x, y):
        self.draw_empty(j, i, x, y)
        self.screen.blit(self.rock_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_water(self, j, i, x, y):
        self.screen.blit(self.water_img, (i*self.width - x*self.width, j*self.height - y*self.height))
