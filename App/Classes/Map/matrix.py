import random
from App.Classes.PathFinding.river_path import PathFinder
from App.Constants.Cells.cells import *

class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.river_path_finder = None
        self.matrix = self.generate_initial_matrix()

    def generate_initial_matrix(self):
        matrix = [[EMPTY for _ in range(self.height)] for _ in range(self.width)]

        #matrix = self.random_rocks(matrix)
        matrix = self.generate_river(matrix)

        return matrix

    def random_rocks(self, matrix):
        i, j = random.randint(1, self.width-1), random.randint(1, self.height-1)

        matrix[i][j] = ROCK

        return matrix
    
    def generate_river(self, matrix):
        self.river_path_finder = PathFinder(matrix, diagonal_movement = True)

        start_j = random.randint(2, self.height-3)
        mid_j = random.randint(2, self.height-3)
        final_j = random.randint(2, self.height-3)

        self.river_path_finder.create_path((0, start_j),(self.width//2, mid_j))
        self.create_river_from_path(matrix)

        self.river_path_finder.create_path((self.width//2, mid_j), (self.width-1, final_j))
        self.create_river_from_path(matrix)

        return matrix
    
    def create_river_from_path(self, matrix):
        for cell in self.river_path_finder.path:
            i = cell.y
            j = cell.x
            matrix[i][j] = WATER
            matrix[i+1][j] = WATER

        return matrix