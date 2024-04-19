from App.Classes.Map.map_builder import MapBuilder
from App.Classes.Map.map_buildings import MapBuildings
from App.Classes.Map.map_interface import MapInterface
from App.Classes.Map.map_movement import MapMovement
from App.Classes.Map.matrix import Matrix
from App.Classes.Penguins.commander import PenguinCommander
from App.Constants.map import *


class Map:
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT, screen=None):
        self.width = width
        self.height = height

        self.matrix = Matrix(self.width, self.height)

        self.buildings = MapBuildings()

        self.interface = MapInterface(self.matrix, self.buildings, screen)

        self.movement = MapMovement(map=self.interface)

        self.builder = MapBuilder(matrix = self.matrix)

        self.penguin_commander = PenguinCommander(buildings = self.buildings, matrix = self.matrix)

    def move(self, keys, mouse_pos, button_clicked, button_released):
        self.movement.move(keys, mouse_pos, button_clicked, button_released)

    def draw(self, mouse_pos, button_clicked, mouse_in_panel):
        self.interface.draw(mouse_pos, button_clicked, self.builder, self.penguin_commander.penguins, mouse_in_panel)