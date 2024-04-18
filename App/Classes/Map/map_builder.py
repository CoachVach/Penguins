from App.Classes.Buildings.Bridge.factory import BridgeFactory
from App.Classes.Buildings.Igloo.factory import IglooFactory
from App.Classes.Buildings.Road.factory import RoadFactory


class MapBuilder:
    def __init__(self, matrix):
        self.matrix = matrix

        self.buildings = [IglooFactory(), RoadFactory(), BridgeFactory()]

        self.selected = None

        self.active = False

    def activate(self, active):
        self.active = active

    def create(self, j, i, buildings):
        self.selected.create(j, i, self.matrix, buildings)