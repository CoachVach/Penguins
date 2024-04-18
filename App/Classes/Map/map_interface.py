from App.Classes.Drawers.cell_drawer import CellDrawer


class MapInterface:
    def __init__(self, matrix, screen=None):
        self.matrix = matrix
        self.screen = screen
        self.cell_drawer = CellDrawer(screen)

        self.x = -5
        self.y = -5

    def draw(self):
        for i, row in enumerate(self.matrix.matrix):
            for j, cell in enumerate(row):
                self.cell_drawer.draw(cell, i, j, self.x, self.y)