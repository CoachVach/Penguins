import pygame
from App.Constants.Penguins.facing import *
from App.Constants.Cells.interface import CELL_HEIGHT, CELL_WIDTH
from App.Constants.Penguins.Images.movement import *
from App.Interface.Images.image_transformer import penguin_imgs

class Penguin:
    def __init__(self, i= 10, j= 10):

        self.i = i
        self.j = j

        self.walking_up_imgs = penguin_imgs(PENGUIN_WALK_UP_IMGS)
        self.walking_down_imgs = penguin_imgs(PENGUIN_WALK_DOWN_IMGS)
        self.walking_right_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS)
        self.walking_left_imgs = penguin_imgs(PENGUIN_WALK_SIDE_IMGS, True)
        self.standing_img = self.walking_down_imgs[0]

        self.facing = STANDING

        self.vel = CELL_WIDTH

        self.food = 100
        self.water = 100

        self.last_decrease_time = pygame.time.get_ticks()
        self.decrease_interval = 5000  # 5000 milliseconds = 5 seconds

        self.path = None

    def draw(self, screen, x, y, counter):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_decrease_time >= self.decrease_interval:
            self.food = max(0, self.food - 1)
            self.water = max(0, self.water - 1)
            self.last_decrease_time = current_time

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
        pos = self.position(x, y, counter)

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
        self.determine_direction()

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