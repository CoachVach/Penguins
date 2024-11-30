from App.Classes.Map.map_builder import MapBuilder
from App.Classes.Map.map_buildings import MapBuildings
from App.Classes.Map.map_interface import MapInterface
from App.Classes.Map.map_movement import MapMovement
from App.Classes.Map.matrix import Matrix
from App.Classes.Penguins.commander import PenguinCommander
from App.Constants.map import *
from App.Constants.Cells.interface import CELL_HEIGHT, CELL_WIDTH


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

        self.selected_building = None
        self.selected_storage = False

    def move(self, keys, mouse_pos, button_clicked, button_released):
        self.movement.move(keys, mouse_pos, button_clicked, button_released)

    def draw(self, mouse_pos, button_clicked, mouse_in_panel):
        if (not self.builder.active and button_clicked and not mouse_in_panel and not self.interface.mouse_in_info_panel(mouse_pos)):
            self.selected_building, self.selected_storage = self.interface.handle_building_selection(mouse_pos)

        self.penguin_commander.handle_penguins()

        self.delete_plants()

        self.interface.draw(mouse_pos, button_clicked, self.builder, self.penguin_commander.penguins, mouse_in_panel, self.selected_building, self.selected_storage)
        
    def delete_plants(self):
        for plant in self.buildings.plants:
            if plant.collected:
                self.buildings.plants.remove(plant)
                return