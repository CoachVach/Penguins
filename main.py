import pygame

from App.Classes.Map.map import Map
from App.Constants.colors import *
from App.Constants.text import *
from App.Interface.Images.map_movement import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(GAME_TITLE)

map = Map(screen=screen)

running = True
while running:
    screen.fill(BLACK) 
    button_clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                button_clicked = True
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.KEYDOWN:
            pass

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]: 
        running = False
    else:
        move_map_with_keys(keys, map.interface)

    map.interface.draw()

    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
