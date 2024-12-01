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
        free_penguins = self.free_penguins()

        for penguin in free_penguins:
            sent_to_plant = False
            sent_to_collect = False
            for plant in self.buildings.plants:
                if plant.mature:
                    self.send_to_harvest(penguin, plant)
                    free_penguins.remove(penguin)
                    sent_to_plant = True
                    break

            if not sent_to_plant:
                for storage in self.buildings.storages:
                    if not storage.empty():
                        for building in self.buildings.buildings_in_construction():
                            if building.construction_materials.name == storage.material.name:
                                self.send_to_collect(penguin, storage)
                                free_penguins.remove(penguin)
                                sent_to_collect = True
                                break
                    if sent_to_collect:
                        break
                                

        material_penguins = self.penguins_with_material()
        print(len(material_penguins))

        for penguin in material_penguins:
            sent_to_build = False  
            print(len(self.buildings.buildings_in_construction()))
            for building in self.buildings.buildings_in_construction():
                if building.construction_materials.name == penguin.material.name:
                    self.send_to_build(penguin, building)
                    material_penguins.remove(penguin)
                    sent_to_build = True
                    break  

            if not sent_to_build:
                for storage in self.buildings.storages:
                    if storage.fillable() and storage.material.name == penguin.material.name:
                        self.send_to_store(penguin, storage)
                        material_penguins.remove(penguin)
                        break  

    def send_penguin(self, penguin, end):
        self.road_matrix = self.create_road_matrix()
        self.path_finder.update_matrix(self.road_matrix)
        penguin.determine_path(self.path_finder.create_path((penguin.i, penguin.j), end))

    def free_penguins(self):
        penguins = []
        for p in self.penguins:
            if not p.busy:
                penguins.append(p)
            
        return penguins
    
    def penguins_with_material(self):
        penguins = []
        for p in self.penguins:
            if not p.building and not p.storing and p.material:
                penguins.append(p)
            
        return penguins
    
    def send_to_harvest(self, penguin, plant):
        self.send_penguin(penguin, (plant.door_i, plant.door_j))
        penguin.harvesting = plant

    def send_to_store(self, penguin, storage):
        self.send_penguin(penguin, (storage.door_i, storage.door_j))
        penguin.storing = storage

    def send_to_build(self, penguin, building):
        self.send_penguin(penguin, (building.door_i, building.door_j))
        penguin.building = building

    def send_to_collect(self, penguin, building):
        self.send_penguin(penguin, (building.door_i, building.door_j))
        penguin.collecting = building


