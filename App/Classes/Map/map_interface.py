import pygame
from App.Classes.Drawers.building_drawer import BuildingDrawer
from App.Classes.Drawers.cell_drawer import CellDrawer
from App.Constants.Cells.interface import *
from App.Constants.colors import RED
from App.Constants.map import *


class MapInterface:
    def __init__(self, matrix, buildings, screen=None):
        self.matrix = matrix
        self.buildings = buildings
        self.screen = screen

        self.cell_drawer = CellDrawer(screen)
        self.building_drawer = BuildingDrawer(screen)

        self.x = -5
        self.y = -5

    def draw(self, mouse_pos, button_clicked, builder, mouse_in_panel):
        self.draw_cells()

        self.draw_buildings()

        self.draw_when_builder(mouse_pos, button_clicked, mouse_in_panel, builder)

    def draw_cells(self):
        for i, row in enumerate(self.matrix.matrix):
            for j, cell in enumerate(row):
                self.cell_drawer.draw(cell, i, j, self.x, self.y)

    def draw_when_builder(self, mouse_pos, button_clicked, mouse_in_panel, builder):
        mouse_x, mouse_y = mouse_pos

        mouse_i = (mouse_x + self.x*CELL_WIDTH) // CELL_WIDTH
        mouse_j = (mouse_y + self.y*CELL_HEIGHT) // CELL_HEIGHT
        
        selected_building = builder.selected
        if not mouse_in_panel and (mouse_i >= 0 and mouse_i < MAP_WIDTH) and (mouse_j >= 0 and mouse_j < MAP_HEIGHT):
            if selected_building == None:
                self.cell_drawer.draw_selected(mouse_j, mouse_i, self.x, self.y)
            else:
                if button_clicked:
                    builder.create(mouse_j, mouse_i, self.buildings)
                else:
                    self.building_drawer.draw_incomplete_building(mouse_j, mouse_i, self.x, self.y, selected_building)

    def draw_buildings(self):
        self.draw_iglooes()

    def draw_iglooes(self):
        for igloo in self.buildings.iglooes:
            igloo.draw(self.screen, self.x, self.y)