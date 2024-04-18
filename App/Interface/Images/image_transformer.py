import pygame

from App.Constants.Cells.interface import *

def transform_img(img, width, height):
    image = pygame.image.load(img)
    alpha_img = image.convert_alpha()
    scaled_img = pygame.transform.scale(alpha_img, (width, height)).convert_alpha()

    return scaled_img

def cell_img(img):
    return transform_img(img, CELL_WIDTH, CELL_HEIGHT)