from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import ROAD
from App.Constants.panel import ROAD_BUTTON_IMG

class RoadFactory(Factory):
    def __init__(self):
        super().__init__(img = ROAD_BUTTON_IMG,button_img = ROAD_BUTTON_IMG, width=1, height=1)

    def create(self, j, i, matrix, buildings):
        matrix.matrix[j][i] = ROAD