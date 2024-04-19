from App.Classes.Buildings.building import Building
from App.Classes.Penguins.penguin import Penguin


class Igloo(Building):
    def __init__(self, j, i, width, height, img, horizontal=True):
        super().__init__(j, i, width, height, img, horizontal)

        self.penguins = [Penguin(self)]

        self.capacity = 1

    def draw(self, screen, x, y, counter):
        super().draw(screen, x, y)
        for penguin in self.penguins:
            penguin.draw(screen, x, y, counter)