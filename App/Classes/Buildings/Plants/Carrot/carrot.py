from App.Classes.Buildings.Plants.plant import Plant
from App.Constants.Buildings.buildings import *

class Carrot(Plant):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, 15, horizontal)
