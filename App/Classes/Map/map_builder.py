from App.Classes.Buildings.Barrel.factory import BarrelFactory
from App.Classes.Buildings.Bridge.factory import BridgeFactory
from App.Classes.Buildings.Igloo.factory import IglooFactory
from App.Classes.Buildings.Plants.Carrot.factory import CarrotFactory
from App.Classes.Buildings.Road.factory import RoadFactory
from App.Classes.Buildings.Soil.factory import SoilFactory
from App.Classes.Buildings.Storage.factory import StorageFactory

class MapBuilder:
    def __init__(self, matrix):
        self.matrix = matrix

        self.buildings = [IglooFactory(), RoadFactory(), BridgeFactory(), BarrelFactory(), StorageFactory()]

        self.plants = [SoilFactory(), CarrotFactory()]

        self.selected = None

        self.active = False

    def activate(self, active):
        self.active = active

    def create(self, j, i, buildings):
        self.selected.create(j, i, self.matrix, buildings)