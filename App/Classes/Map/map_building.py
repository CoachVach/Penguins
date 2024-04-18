from App.Classes.Buildings.Igloo.factory import IglooFactory


class MapBuilder:
    def __init__(self, matrix):
        self.matrix = matrix

        self.buildings = [IglooFactory()]

        self.active = False

    def activate(self, active):
        self.active = active