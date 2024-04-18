from App.Constants.Cells.cells import *
from App.Constants.Cells.interface import *
from App.Interface.Images.image_transformer import cell_img


class CellDrawer:
    def __init__(self, screen):
        self.screen = screen

        self.empty_img = cell_img(EMPTY_IMG)
        self.rock_img = cell_img(ROCK_IMG)
    
    def draw(self, cell, j, i):
        if cell == EMPTY:
            self.draw_empty(j, i)
        elif cell == ROCK:
            self.draw_rock(j, i)

    def draw_empty(self, j, i):
        pass

    def draw_rock(self, j, i):
        pass
