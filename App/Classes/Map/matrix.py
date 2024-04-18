from App.Constants.Cells.cells import EMPTY

class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.matrix = self.generate_initial_matrix()

    def generate_initial_matrix(self):
        return [[EMPTY for _ in range(self.height)] for _ in range(self.width)]
