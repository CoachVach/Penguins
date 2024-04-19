from App.Classes.Buildings.building import Building
from App.Constants.Buildings.buildings import *

class Plant(Building):
    def __init__(self, j, i, width, height, img, horizontal=True):
        super().__init__(j, i, width, height, img, horizontal)
