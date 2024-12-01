from App.Classes.Buildings.building import Building
from App.Classes.Material.Wood.wood import Wood

class Barrel(Building):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, Wood(2), horizontal)