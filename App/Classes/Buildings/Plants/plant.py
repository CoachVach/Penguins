import threading

import pygame
from App.Classes.Buildings.building import Building
from App.Constants.Buildings.buildings import *
from App.Constants.Cells.interface import CELL_HEIGHT, CELL_WIDTH
from App.Constants.colors import *
from App.Constants.interface import DELAY

class Plant(Building):
    def __init__(self, j, i, width, height, img, door_j, door_i, seconds = 10, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, horizontal)

        self.timer = threading.Timer(seconds, self.set_mature)
        self.timer.start()
        
        self.maturity_w = 5
        self.maturity_h = 0
        self.growth_rate = CELL_WIDTH / ((seconds*1000)/DELAY)

        self.mature = False
        self.collected = False

    def set_mature(self):
        self.mature = True

    def draw(self, screen, x, y):
        super().draw(screen, x, y)

        maturity_rect = (self.i*CELL_WIDTH - x*CELL_WIDTH, self.j*CELL_HEIGHT - y*CELL_HEIGHT, 5, CELL_HEIGHT)
        if not self.mature:
            self.maturity_h += self.growth_rate
            color = RED
        else:
            color = GREEN

        maturity_rect = (self.i*CELL_WIDTH - x*CELL_WIDTH, (self.j*CELL_HEIGHT - y*CELL_HEIGHT + CELL_HEIGHT - self.maturity_h ), self.maturity_w, self.maturity_h)
        pygame.draw.rect(screen, color, maturity_rect)
