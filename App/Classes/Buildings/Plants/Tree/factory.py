from App.Classes.Buildings.Plants.Tree.tree import Tree
from App.Classes.Buildings.Plants.factory import PlantFactory
from App.Constants.Plants.plants import TREE_IMG
from App.Constants.orientation import HORIZONTAL
from App.Constants.panel import TREE_BUTTON_IMG

class TreeFactory(PlantFactory):
    def __init__(self):
        super().__init__(img = TREE_IMG, button_img = TREE_BUTTON_IMG)

    def create(self, j, i, matrix, buildings, door_i, door_j):
        super().create( j, i, matrix, buildings, door_i, door_j)
        
        buildings.plants.append(Tree(j, i, self.width, self.height, self.img, door_j, door_i, self.orientation == HORIZONTAL))
