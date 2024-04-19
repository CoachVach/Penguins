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
    
    def send_penguin(self, end):
        self.road_matrix = self.create_road_matrix()
        self.path_finder.update_matrix(self.road_matrix)
        penguin = self.penguins[0]
        penguin.determine_path(self.path_finder.create_path((penguin.i, penguin.j), end))



