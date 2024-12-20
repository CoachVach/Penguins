from App.Classes.Buildings.Igloo.igloo import Igloo
from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import IGLOO
from App.Constants.Buildings.images import IGLOO_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import IGLOO_BUTTON_IMG

class IglooFactory(Factory):
    def __init__(self):
        super().__init__(img = IGLOO_IMG, button_img = IGLOO_BUTTON_IMG, width=3, height=3)

    def create(self, j, i, matrix, buildings, door_i, door_j):
        for row in range(j, j + self.width):
            for col in range(i, i + self.height):
                matrix.matrix[row][col] = IGLOO

        buildings.iglooes.append(Igloo(j, i, self.width, self.height, self.img, door_j, door_i, self.orientation == HORIZONTAL))

