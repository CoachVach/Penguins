import pygame

from App.Constants.Cells.interface import *
from App.Constants.panel import *

def transform_img(img, width, height, transparency=255):
    image = pygame.image.load(img)
    alpha_img = image.convert_alpha()
    scaled_img = pygame.transform.scale(alpha_img, (width, height)).convert_alpha()
    scaled_img.set_alpha(transparency)

    return scaled_img

def cell_img(img):
    return transform_img(img, CELL_WIDTH, CELL_HEIGHT)

def panel_button_img(img):
    return transform_img(img, PANEL_BUTTON_WIDTH, PANEL_BUTTON_HEIGHT)

def incomplete_building_img(img, width, height):
    return transform_img(img, width, height, 180)

def building_img(img, width, height):
    return transform_img(img, width, height)