import pygame

from App.Classes.Map.map import Map
from App.Classes.Panel.panel import Panel
from App.Constants.colors import *
from App.Constants.text import *
from App.Classes.Map.map_movement import *

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(GAME_TITLE)

map = Map(screen=screen)
panel = Panel(screen=screen, map=map)

running = True
while running:
    screen.fill(BLACK) 
    button_clicked = False
    button_released = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                button_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                button_released = True
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.KEYDOWN:
            pass

    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]: 
        running = False
    else:
        map.move(keys, mouse_pos, button_clicked, button_released)

    map.draw(mouse_pos, button_clicked, panel.mouse_in_panel(mouse_pos))
    panel.draw(mouse_pos, button_clicked)

    pygame.display.flip()

    pygame.time.delay(75)

pygame.quit()
