from App.Constants.Cells.cells import EMPTY, ROAD
from App.Constants.orientation import *


class Factory:
    def __init__(self, img, button_img, width, height):
        self.img = img
        self.button_img = button_img

        self.orientation = HORIZONTAL

        self.width = width
        self.height = height

    def has_adjacent_road(self, j, i, matrix):
        # Check all adjacent cells for a road

        for x in range(i, i + self.width):
            for y in range(j, j + self.height):
                adjacent_positions = [
                    (y-1, x),  # arriba
                    (y+1, x),  # abajo
                    (y, x-1),  # izquierda
                    (y, x+1)   # derecha
                ]
                for adj_j, adj_i in adjacent_positions:
                    if (0 <= adj_j < len(matrix.matrix[0]) and 
                        0 <= adj_i < len(matrix.matrix) and 
                        matrix.matrix[adj_i][adj_j] == ROAD):
                        return True, adj_j, adj_i
        return False, 0, 0

    def can_build(self, i, j, matrix):
        adj_road, adj_i, adj_j = self.has_adjacent_road(j, i, matrix)
        if not adj_road:
            return False, 0, 0
            
        # Check if the area is clear
        for x in range(i, i + self.width):
            for y in range(j, j + self.height):
                if (x >= len(matrix.matrix) or 
                    y >= len(matrix.matrix[0]) or 
                    not matrix.matrix[x][y]==EMPTY):
                    return False, 0, 0
        return True, adj_i, adj_j
    
    def rotate(self):
        self.orientation = VERTICAL if self.orientation == HORIZONTAL else HORIZONTAL

        w_aux = self.width
        self.width = self.height
        self.height = w_aux