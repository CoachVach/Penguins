from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import *
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import BRIDGE_BUTTON_IMG

class BridgeFactory(Factory):
    def __init__(self):
        super().__init__(img = BRIDGE_BUTTON_IMG,button_img = BRIDGE_BUTTON_IMG, width=1, height=1)

    def create(self, j, i, matrix, buildings, door_i = 0, door_j = 0):
        cell = HORIZONTAL_BRIDGE if self.orientation == HORIZONTAL else VERTICAL_BRIDGE
        matrix.matrix[j][i] = cell

    def can_build(self, j, i, matrix):
        return (matrix.matrix[j][i] == WATER), 0, 0