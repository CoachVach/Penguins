from App.Classes.PathFinding.river_path import PathFinder
from App.Classes.Penguins.penguin import Penguin
from App.Constants.Cells.cells import ROAD


class PenguinCommander:
    def __init__(self, buildings=None, matrix = None):
        self.buildings = buildings
        self.matrix = matrix

        self.road_matrix = self.create_road_matrix()

        self.penguins = [Penguin()]

        self.path_finder = PathFinder(self.road_matrix)

    def create_road_matrix(self):
        matrix = self.matrix.matrix
        road_matrix =  [[0 for _ in range(self.matrix.height)] for _ in range(self.matrix.width)]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == ROAD:
                    road_matrix[row][col] = 1

        return road_matrix
    
    def handle_penguins(self):
        free_penguin = self.free_penguin()

        if free_penguin:
            for plant in self.buildings.plants:
                if plant.mature:
                    self.send_to_harvest(free_penguin, plant)
                    break
        
        material_penguin = self.penguin_with_material()

        if material_penguin:
            for storage in self.buildings.storages:
                if (storage.material.name == material_penguin.material.name) and not storage.full():
                    self.send_to_store(material_penguin, storage)

    
    def send_penguin(self, penguin, end):
        self.road_matrix = self.create_road_matrix()
        self.path_finder.update_matrix(self.road_matrix)
        penguin.determine_path(self.path_finder.create_path((penguin.i, penguin.j), end))

    def free_penguin(self):
        for p in self.penguins:
            if not p.busy:
                return p
            
        return None
    
    def penguin_with_material(self):
        for p in self.penguins:

            if not p.storing and p.material:
                return p
            
        return None
    
    def send_to_harvest(self, penguin, plant):
        self.send_penguin(penguin, (plant.door_i, plant.door_j))
        penguin.harvesting = plant

    def send_to_store(self, penguin, storage):
        self.send_penguin(penguin, (storage.door_i, storage.door_j))
        penguin.storing = storage


