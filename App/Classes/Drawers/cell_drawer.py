import pygame
from App.Constants.Cells.cells import *
from App.Constants.Cells.interface import *
from App.Constants.colors import *
from App.Interface.Images.image_transformer import cell_img


class CellDrawer:
    def __init__(self, screen):
        self.screen = screen

        self.width = CELL_WIDTH
        self.height = CELL_HEIGHT

        self.empty_img = cell_img(EMPTY_IMG)
        self.rock_img = cell_img(ROCK_IMG)
        self.water_img = cell_img(WATER_IMG)
        self.road_img = cell_img(ROAD_IMG)
        self.bridge_img = cell_img(BRIDGE_IMG)
        self.soil_img = cell_img(SOIL_IMG)
    
    def draw(self, cell, j, i, x, y):
        if cell == EMPTY or cell == IGLOO or cell == BARREL or cell == STORAGE:
            self.draw_empty(j, i, x, y)
        elif cell == ROCK:
            self.draw_rock(j, i, x, y)
        elif cell == WATER:
            self.draw_water(j, i, x, y)
        elif cell == ROAD:
            self.draw_road(j, i, x, y)
        elif cell == HORIZONTAL_BRIDGE:
            self.draw_bridge(j, i, x, y, True)
        elif cell == VERTICAL_BRIDGE:
            self.draw_bridge(j, i, x, y, False)
        elif cell == SOIL:
            self.draw_soil(j, i, x, y)

    def draw_empty(self, j, i, x, y):
        self.screen.blit(self.empty_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_rock(self, j, i, x, y):
        self.draw_empty(j, i, x, y)
        self.screen.blit(self.rock_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_water(self, j, i, x, y):
        self.screen.blit(self.water_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_road(self, j, i, x, y):
        self.screen.blit(self.road_img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_bridge(self, j, i, x, y, horizontal):
        self.draw_water(j, i, x, y)
        if not horizontal:
            img = pygame.transform.rotate(self.bridge_img, 90)
        else:
            img = self.bridge_img
        self.screen.blit(img, (i*self.width - x*self.width, j*self.height - y*self.height))

    def draw_soil(self, j, i, x, y):
        self.screen.blit(self.soil_img, (i*self.width - x*self.width, j*self.height - y*self.height))
    
    def draw_selected(self, j, i, x, y):
        s = pygame.Surface((self.width, self.height))
        s.set_alpha(100)
        s.fill(GREEN)
        self.screen.blit(s, (i*self.width - x*self.width, j*self.height - y*self.height))