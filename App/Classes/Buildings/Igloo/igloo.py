from App.Classes.Buildings.building import Building
from App.Classes.Penguins.penguin import Penguin


class Igloo(Building):
    def __init__(self, j, i, width, height, img, horizontal=True):
        super().__init__(j, i, width, height, img, horizontal)

        self.capacity = 1
