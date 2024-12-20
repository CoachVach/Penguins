
from App.Classes.Buildings.Storage.storage import Storage
from App.Classes.Factory.factory import Factory
from App.Constants.Cells.cells import STORAGE
from App.Constants.Buildings.images import STORAGE_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import STORAGE_BUTTON_IMG

class StorageFactory(Factory):
    def __init__(self):
        super().__init__(img = STORAGE_IMG, button_img = STORAGE_BUTTON_IMG, width=3, height=3)

    def create(self, j, i, matrix, buildings, door_i, door_j):
        for row in range(j, j + self.width):
            for col in range(i, i + self.height):
                matrix.matrix[row][col] = STORAGE

        buildings.storages.append(Storage(j, i, self.width, self.height, self.img, door_j, door_i, self.orientation == HORIZONTAL))

