
from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import PLANT, SOIL

class PlantFactory(Factory):
    def __init__(self, img, button_img):
        super().__init__(img = img, button_img = button_img, width=1, height=1)

    def create(self, j, i, matrix, buildings, door_i = 0, door_j = 0):
        matrix.matrix[j][i] = PLANT

    def can_build(self, j, i, matrix):
        return (matrix.matrix[j][i] == SOIL), 0, 0
