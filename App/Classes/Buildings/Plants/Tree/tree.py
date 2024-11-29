from App.Classes.Buildings.Plants.plant import Plant
from App.Constants.Buildings.buildings import *

class Tree(Plant):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, 30, horizontal)
