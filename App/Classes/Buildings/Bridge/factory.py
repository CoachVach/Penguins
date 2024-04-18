from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import BRIDGE
from App.Constants.panel import BRIDGE_BUTTON_IMG

class BridgeFactory(Factory):
    def __init__(self):
        super().__init__(img = BRIDGE_BUTTON_IMG,button_img = BRIDGE_BUTTON_IMG, width=1, height=1)

    def create(self, j, i, matrix, buildings):
        matrix.matrix[j][i] = BRIDGE