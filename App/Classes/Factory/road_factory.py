from App.Constants.Cells.cells import EMPTY, ROAD
from App.Constants.orientation import *


class RoadFactory:
    def __init__(self, img, button_img, width, height):
        self.img = img
        self.button_img = button_img

        self.orientation = HORIZONTAL

        self.width = width
        self.height = height

    def can_build(self, i, j, matrix):
            
        # Check if the area is clear
        for x in range(i, i + self.width):
            for y in range(j, j + self.height):
                if (x >= len(matrix.matrix) or 
                    y >= len(matrix.matrix[0]) or 
                    not matrix.matrix[x][y]==EMPTY):
                    return False, 0, 0
        return True, 0, 0
    
    def rotate(self):
        self.orientation = VERTICAL if self.orientation == HORIZONTAL else HORIZONTAL

        w_aux = self.width
        self.width = self.height
        self.height = w_aux