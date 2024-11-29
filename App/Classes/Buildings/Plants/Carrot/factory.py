
from App.Classes.Buildings.Plants.Carrot.carrot import Carrot
from App.Classes.Buildings.Plants.factory import PlantFactory
from App.Constants.Plants.plants import CARROT_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import CARROT_BUTTON_IMG

class CarrotFactory(PlantFactory):
    def __init__(self):
        super().__init__(img = CARROT_IMG, button_img = CARROT_BUTTON_IMG)

    def create(self, j, i, matrix, buildings, door_i, door_j):
        super().create( j, i, matrix, buildings, door_i, door_j)
        
        buildings.plants.append(Carrot(j, i, self.width, self.height, self.img, door_j, door_i, self.orientation == HORIZONTAL))
