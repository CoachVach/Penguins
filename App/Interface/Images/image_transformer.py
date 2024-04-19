import pygame

from App.Constants.Cells.interface import *
from App.Constants.panel import *

def transform_img(img, width, height, transparency=255, horizontal=True):
    image = pygame.image.load(img)
    alpha_img = image.convert_alpha()
    scaled_img = pygame.transform.scale(alpha_img, (width, height)).convert_alpha()
    scaled_img.set_alpha(transparency)
    if not horizontal:
        scaled_img = pygame.transform.rotate(scaled_img, 90)

    return scaled_img

def cell_img(img, horizontal=True):
    return transform_img(img, CELL_WIDTH, CELL_HEIGHT, horizontal=horizontal)

def panel_button_img(img):
    return transform_img(img, PANEL_BUTTON_WIDTH, PANEL_BUTTON_HEIGHT)

def incomplete_building_img(img, width, height, horizontal=True):
    return transform_img(img, width, height, 180, horizontal=horizontal)

def unbuildable_building_img(img, width, height, horizontal=True):
    return transform_img(img, width, height, 50, horizontal=horizontal)

def building_img(img, width, height, horizontal=True):
    return transform_img(img, width, height, horizontal=horizontal)