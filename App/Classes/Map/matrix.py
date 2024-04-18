import random
from App.Constants.Cells.cells import *

class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.matrix = self.generate_initial_matrix()

    def generate_initial_matrix(self):
        matrix = [[EMPTY for _ in range(self.height)] for _ in range(self.width)]

        matrix = self.random_rocks(matrix)

        return matrix

    def random_rocks(self, matrix):
        i, j = random.randint(1, self.width-1), random.randint(1, self.height-1)

        matrix[i][j] = ROCK

        return matrix