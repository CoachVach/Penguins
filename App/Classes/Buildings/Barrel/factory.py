
from App.Classes.Buildings.Barrel.barrel import Barrel
from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import BARREL
from App.Constants.Buildings.images import BARREL_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import BARREL_BUTTON_IMG

class BarrelFactory(Factory):
    def __init__(self):
        super().__init__(img = BARREL_IMG, button_img = BARREL_BUTTON_IMG, width=1, height=1)

    def create(self, j, i, matrix, buildings):
        for row in range(j, j + self.width):
            for col in range(i, i + self.height):
                matrix.matrix[row][col] = BARREL

        buildings.barrels.append(Barrel(j, i, self.width, self.height, self.img, self.orientation == HORIZONTAL))

