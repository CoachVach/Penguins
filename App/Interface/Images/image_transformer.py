import pygame

from App.Constants.Cells.interface import *

def transform_img(img, width, height):
    image = pygame.image.load(img).convert_alpha()
    alpha_img = pygame.image.load(image).convert_alpha()
    scaled_img = pygame.transform.scale(alpha_img, (width, height))

    return scaled_img

def cell_img(img):
    transform_img(img, CELL_WIDTH, CELL_HEIGHT)