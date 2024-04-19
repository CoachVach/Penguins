from App.Classes.Buildings.building import Building
from App.Constants.Buildings.buildings import *

class Storage(Building):
    def __init__(self, j, i, width, height, img, horizontal=True):
        super().__init__(j, i, width, height, img, horizontal)

        self.elements = 0

        self.capacity = STORAGE_CAPACITY

    def add_element(self, amount=1):
        if((self.elements + amount) <= self.capacity):
            self.elements += amount
        else:
            self.elements = self.capacity