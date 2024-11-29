
from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import PLANT, ROAD, SOIL

class PlantFactory(Factory):
    def __init__(self, img, button_img):
        super().__init__(img = img, button_img = button_img, width=1, height=1)

    def create(self, j, i, matrix, buildings, door_i, door_j):
        matrix.matrix[j][i] = PLANT

    def can_build(self, j, i, matrix):
        if matrix.matrix[j][i] == SOIL:
            door_i , door_j = self.find_door(i, j, matrix)
        else:
            return False, 0, 0
        return (matrix.matrix[j][i] == SOIL), door_i , door_j
    
    def find_door(self,y, x, matrix):
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
                return adj_j, adj_i
            
        return 0,0
