from App.Classes.Buildings.building import Building

class Barrel(Building):
    def __init__(self, j, i, width, height, img, horizontal=True):
        super().__init__(j, i, width, height, img, horizontal)