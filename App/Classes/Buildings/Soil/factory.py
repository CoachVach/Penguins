from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import SOIL
from App.Constants.panel import SOIL_BUTTON_IMG

class SoilFactory(Factory):
    def __init__(self):
        super().__init__(img = SOIL_BUTTON_IMG,button_img = SOIL_BUTTON_IMG, width=1, height=1)

    def create(self, j, i, matrix, buildings, door_i = 0, door_j = 0):
        matrix.matrix[j][i] = SOIL