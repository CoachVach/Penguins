from App.Classes.Drawers.building_drawer import BuildingDrawer
from App.Classes.Drawers.cell_drawer import CellDrawer
from App.Constants.Cells.interface import *
from App.Constants.colors import RED
from App.Constants.map import *
from App.Classes.Panel.info_panel import InfoPanel


class MapInterface:
    def __init__(self, matrix, buildings, screen=None):
        self.matrix = matrix
        self.buildings = buildings
        self.screen = screen

        self.cell_drawer = CellDrawer(screen)
        self.building_drawer = BuildingDrawer(screen)

        self.x = -5
        self.y = -5

        self.counter = 0

        self.info_panel = InfoPanel(screen)

    def draw(self, mouse_pos, button_clicked, builder, penguins, mouse_in_panel, selected_building):
        self.draw_cells()

        self.draw_buildings()

        self.info_panel.set_building(selected_building)

        self.draw_when_builder(mouse_pos, button_clicked, mouse_in_panel, builder)

        self.draw_penguins(penguins)

        self.info_panel.draw()
        if self.info_panel.selected_building:
            self.info_panel.selected_building.draw_door(self.screen, self.x, self.y)
            

        self.increment_counter()

    def draw_cells(self):
        for i, row in enumerate(self.matrix.matrix):
            for j, cell in enumerate(row):
                self.cell_drawer.draw(cell, i, j, self.x, self.y)

    def draw_when_builder(self, mouse_pos, button_clicked, mouse_in_panel, builder):
        mouse_x, mouse_y = mouse_pos

        mouse_i = (mouse_x + self.x*CELL_WIDTH) // CELL_WIDTH
        mouse_j = (mouse_y + self.y*CELL_HEIGHT) // CELL_HEIGHT
        
        selected_building = builder.selected
        if (not mouse_in_panel) and (mouse_i >= 0 and mouse_i < MAP_WIDTH) and (mouse_j >= 0 and mouse_j < MAP_HEIGHT):
            if selected_building == None:
                self.cell_drawer.draw_selected(mouse_j, mouse_i, self.x, self.y)
            else:
                can_build, door_i, door_j = selected_building.can_build(mouse_j, mouse_i, self.matrix)
                if can_build:
                    if button_clicked:
                        builder.create(mouse_j, mouse_i, self.buildings, door_i, door_j)
                    else:
                        self.building_drawer.draw_incomplete_building(mouse_j, mouse_i, self.x, self.y, selected_building)
                else:
                    self.building_drawer.draw_unbuildable_building(mouse_j, mouse_i, self.x, self.y, selected_building)

    def draw_buildings(self):
        self.draw_iglooes()
        self.draw_barrels()
        self.draw_storages()
        self.draw_plants()

    def draw_iglooes(self):
        for igloo in self.buildings.iglooes:
            igloo.draw(self.screen, self.x, self.y)

    def draw_barrels(self):
        for barrel in self.buildings.barrels:
            barrel.draw(self.screen, self.x, self.y)

    def draw_storages(self):
        for storage in self.buildings.storages:
            storage.draw(self.screen, self.x, self.y)

    def draw_plants(self):
        for plant in self.buildings.plants:
            plant.draw(self.screen, self.x, self.y)

    def draw_penguins(self, penguins):
        for penguin in penguins:
            penguin.draw(self.screen, self.x, self.y, self.counter)

    def increment_counter(self):
        self.counter += 1
        if self.counter >= 1000:
            self.counter = 0

    def handle_building_selection(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        mouse_i = (mouse_x + self.x*CELL_WIDTH) // CELL_WIDTH
        mouse_j = (mouse_y + self.y*CELL_HEIGHT) // CELL_HEIGHT
        
        selected_building = None
        
        # Revisar todos los tipos de buildings
        for igloo in self.buildings.iglooes:
            # Verificar si el click está dentro del área del building
            if (mouse_i >= igloo.i and mouse_i < igloo.i + igloo.width and 
                mouse_j >= igloo.j and mouse_j < igloo.j + igloo.height):
                selected_building = igloo
                break
                
        for barrel in self.buildings.barrels:
            if (mouse_i >= barrel.i and mouse_i < barrel.i + barrel.width and 
                mouse_j >= barrel.j and mouse_j < barrel.j + barrel.height):
                selected_building = barrel
                break
                
        for storage in self.buildings.storages:
            if (mouse_i >= storage.i and mouse_i < storage.i + storage.width and 
                mouse_j >= storage.j and mouse_j < storage.j + storage.height):
                selected_building = storage
                break
                
        for plant in self.buildings.plants:
            if (mouse_i >= plant.i and mouse_i < plant.i + plant.width and 
                mouse_j >= plant.j and mouse_j < plant.j + plant.height):
                selected_building = plant
                break
        
        return selected_building