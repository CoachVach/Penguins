import pygame
from App.Constants.Cells.interface import *
from App.Constants.colors import BLUE, GREEN, RED
from App.Interface.Images.image_transformer import building_img

class Building:
    def __init__(self, j, i, width, height, img, door_j = 0, door_i = 0, construction_materials = None, horizontal = True):
        self.j = j
        self.i = i

        self.width = width
        self.height = height

        self.door_j = door_j
        self.door_i = door_i

        self.construction_materials = construction_materials

        self.img = building_img(img, self.width*CELL_WIDTH, self.height*CELL_HEIGHT, horizontal)

    def draw(self, screen, x, y):
        screen.blit(self.img, (self.i*CELL_WIDTH - x*CELL_WIDTH, self.j*CELL_HEIGHT - y*CELL_HEIGHT))

    def draw_door(self, screen, x, y):
        s = pygame.Surface((CELL_WIDTH,CELL_HEIGHT))
        s.set_alpha(100)
        s.fill(BLUE)
        screen.blit(s, (self.door_i*CELL_WIDTH - x*CELL_WIDTH, self.door_j*CELL_HEIGHT - y*CELL_HEIGHT))

    def constructed(self):
        return (not self.construction_materials) or (self.construction_materials.cant == 0)
    
    def construct(self, material):
        if (material.name == self.construction_materials.name):
            previous_mat = self.construction_materials.cant
            self.construction_materials.cant -= material.cant
            if (self.construction_materials.cant < 0):
                material.cant -= previous_mat
                self.construction_materials = None
                return material
            else: 
                return None
        else:
            return material
