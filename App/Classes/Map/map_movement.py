import pygame

from App.Constants.Cells.interface import  *

class MapMovement:
    def __init__(self, map):
        self.map = map

        self.pivot = None

    def move(self, keys, mouse_pos, button_clicked, button_released):
        if button_clicked:
            self.pivot = mouse_pos
        elif button_released:
            self.pivot = None
        elif self.pivot != None:
            self.move_map_with_mouse(mouse_pos)
        else:
            self.move_map_with_keys(keys)

    def move_map_with_mouse(self, mouse_pos):
        mousex, mousey = mouse_pos
        pivotx, pivoty = self.pivot
        if abs(mousex-pivotx) > CELL_WIDTH/2:
            self.pivot = mouse_pos
            self.map.x += 1 *(-1 if (mousex-pivotx)>0 else 1)
        if abs(mousey-pivoty) > CELL_HEIGHT/2:
            self.pivot = mouse_pos
            self.map.y += 1 *(-1 if (mousey-pivoty)>0 else 1)

    def move_map_with_keys(self, keys):
        if keys[pygame.K_UP]:
            self.map.y -= 1
        elif keys[pygame.K_DOWN]:
            self.map.y += 1
        elif keys[pygame.K_LEFT]:
            self.map.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.map.x += 1