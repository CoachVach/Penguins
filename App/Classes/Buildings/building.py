import pygame
from App.Constants.Cells.interface import *
from App.Constants.colors import GREEN
from App.Interface.Images.image_transformer import building_img

class Building:
    def __init__(self, j, i, width, height, img, door_j = 0, door_i = 0, horizontal = True):
        self.j = j
        self.i = i
        self.width = width
        self.height = height
        self.door_j = door_j
        self.door_i = door_i
        self.img = building_img(img, self.width*CELL_WIDTH, self.height*CELL_HEIGHT, horizontal)

    def draw(self, screen, x, y):
        screen.blit(self.img, (self.i*CELL_WIDTH - x*CELL_WIDTH, self.j*CELL_HEIGHT - y*CELL_HEIGHT))
