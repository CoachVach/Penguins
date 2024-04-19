from App.Constants.Cells.cells import EMPTY
from App.Constants.orientation import *


class Factory:
    def __init__(self, img, button_img, width, height):
        self.img = img
        self.button_img = button_img

        self.orientation = HORIZONTAL

        self.width = width
        self.height = height

    def can_build(self, j, i, matrix):
        for row in range(j, j + self.width):
            for col in range(i, i + self.height):
                if matrix.matrix[row][col] != EMPTY:
                    return False
                
        return True
    
    def rotate(self):
        self.orientation = VERTICAL if self.orientation == HORIZONTAL else HORIZONTAL

        w_aux = self.width
        self.width = self.height
        self.height = w_aux