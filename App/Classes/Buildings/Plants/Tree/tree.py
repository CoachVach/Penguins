from App.Classes.Buildings.Plants.plant import Plant
from App.Classes.Material.Wood.wood import Wood

class Tree(Plant):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, Wood(5), 30, horizontal)
