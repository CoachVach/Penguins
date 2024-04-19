
import pygame
from App.Constants.Penguins.facing import *
from App.Constants.Cells.interface import CELL_HEIGHT, CELL_WIDTH
from App.Constants.Penguins.Images.movement import *
from App.Interface.Images.image_transformer import penguin_imgs

class Penguin:
    def __init__(self):

        self.i = 10
        self.j = 10

        self.walking_up_imgs = penguin_imgs(PENGUIN_WALK_UP_IMGS)
        self.walking_down_imgs = penguin_imgs(PENGUIN_WALK_DOWN_IMGS)
        self.walking_right_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS)
        self.walking_left_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS, True)
        self.standing_img = self.walking_down_imgs[0]

        self.facing = LEFT

        self.vel = CELL_WIDTH

        self.path = None

    def draw(self, screen, x, y, counter):
        if self.facing == DOWN:
            imgs = self.walking_down_imgs
        elif self.facing == UP:
            imgs = self.walking_up_imgs
        elif self.facing == LEFT:
            imgs = self.walking_left_imgs
        elif self.facing == RIGHT:
            imgs = self.walking_right_imgs
        else:
            imgs = [self.standing_img]

        img = imgs[counter % len(imgs)]

        if self.facing != STANDING:
            pos = self.position(x, y, counter)
        else:
            pos = (self.i*CELL_WIDTH - x*CELL_WIDTH, self.j*CELL_HEIGHT - y*CELL_HEIGHT)

        screen.blit(img, pos)

    def position(self, x, y, counter):
        offset = counter % self.vel

        pos_x = self.i*CELL_WIDTH

        pos_y = self.j*CELL_HEIGHT

        cell_change = offset + 1 == self.vel

        if self.facing == DOWN:
            pos_y += offset
            self.j += 1 if cell_change else 0
        elif self.facing == UP:
            pos_y -= offset
            self.j -= 1 if cell_change else 0
        elif self.facing == LEFT:
            pos_x -= offset
            self.i -= 1 if cell_change else 0
        elif self.facing == RIGHT:
            pos_x += offset
            self.i += 1 if cell_change else 0

        if (cell_change and self.path != None):
            self.determine_direction()

        return (pos_x - x*CELL_WIDTH, pos_y - y*CELL_HEIGHT)

    def determine_path(self, path):
        self.path = path

    def determine_direction(self):
        if len(self.path) >= 1:
            next_cell = self.path[0]
            if next_cell.x > self.i:
                self.facing = RIGHT
            elif next_cell.x < self.i:
                self.facing = LEFT
            elif next_cell.y > self.j:
                self.facing = DOWN
            elif next_cell.y < self.j:
                self.facing = UP

            self.path = self.path[1:]

            if self.path == []:
                self.facing = STANDING