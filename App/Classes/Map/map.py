from App.Classes.Map.map_interface import MapInterface
from App.Classes.Map.map_movement import MapMovement
from App.Classes.Map.matrix import Matrix
from App.Constants.map import *


class Map:
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT, screen=None):
        self.width = width
        self.height = height

        self.matrix = Matrix(self.width, self.height)

        self.interface = MapInterface(self.matrix, screen)

        self.movement = MapMovement(map=self.interface)

    def move(self, keys, mouse_pos, button_clicked, button_released):
        self.movement.move(keys, mouse_pos, button_clicked, button_released)