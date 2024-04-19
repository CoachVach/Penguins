import pygame
from App.Constants.Cells.cells import *
from App.Constants.Cells.interface import *
from App.Constants.colors import *
from App.Interface.Images.image_transformer import *

class BuildingDrawer:
    def __init__(self, screen):
        self.screen = screen

        self.empty_img = cell_img(EMPTY_IMG)
        self.rock_img = cell_img(ROCK_IMG)
        self.water_img = cell_img(WATER_IMG)
    
    def draw_incomplete_building(self, j, i, x, y, building):
        img = incomplete_building_img(building.img, building.width*CELL_WIDTH, building.height*CELL_HEIGHT)
        self.screen.blit(img, (i*CELL_WIDTH - x*CELL_WIDTH, j*CELL_HEIGHT - y*CELL_HEIGHT))

    def draw_unbuildable_building(self, j, i, x, y, building):
        img = unbuildable_building_img(building.img, building.width*CELL_WIDTH, building.height*CELL_HEIGHT)
        self.screen.blit(img, (i*CELL_WIDTH - x*CELL_WIDTH, j*CELL_HEIGHT - y*CELL_HEIGHT))