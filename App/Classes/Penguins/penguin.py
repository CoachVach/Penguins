
import pygame
from App.Classes.Penguins.facing import *
from App.Constants.Cells.interface import CELL_HEIGHT, CELL_WIDTH
from App.Constants.Penguins.Images.movement import *
from App.Interface.Images.image_transformer import penguin_imgs


class Penguin:
    def __init__(self, igloo):
        self.igloo = igloo

        self.i = igloo.i
        self.j = igloo.j

        self.walking_up_imgs = penguin_imgs(PENGUIN_WALK_UP_IMGS)
        self.walking_down_imgs = penguin_imgs(PENGUIN_WALK_DOWN_IMGS)
        self.walking_right_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS)
        self.walking_left_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS, True)

        self.facing = LEFT
        
    def draw(self, screen, x, y, counter):
        if self.facing == DOWN:
            imgs = self.walking_down_imgs
        elif self.facing == UP:
            imgs = self.walking_up_imgs
        elif self.facing == LEFT:
            imgs = self.walking_left_imgs
        elif self.facing == RIGHT:
            imgs = self.walking_right_imgs

        img = imgs[counter % len(imgs)]

        screen.blit(img, (self.i*CELL_WIDTH - x*CELL_WIDTH, self.j*CELL_HEIGHT - y*CELL_HEIGHT))