
from App.Classes.Buildings.Plants.Carrot.carrot import Carrot
from App.Classes.Buildings.Plants.factory import PlantFactory
from App.Constants.Cells.cells import PLANT, SOIL
from App.Constants.Plants.plants import CARROT_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import CARROT_BUTTON_IMG

class CarrotFactory(PlantFactory):
    def __init__(self):
        super().__init__(img = CARROT_IMG, button_img = CARROT_BUTTON_IMG)

    def create(self, j, i, matrix, buildings , door_i = 0, door_j = 0):
        super().create( j, i, matrix, buildings)
        
        buildings.plants.append(Carrot(j, i, self.width, self.height, self.img, self.orientation == HORIZONTAL))
