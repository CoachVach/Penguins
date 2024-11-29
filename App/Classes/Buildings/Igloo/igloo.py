from App.Classes.Buildings.building import Building
from App.Classes.Penguins.penguin import Penguin


class Igloo(Building):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, horizontal)

        self.capacity = 1
