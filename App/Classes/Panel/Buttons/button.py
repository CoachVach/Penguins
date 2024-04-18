import pygame

from App.Constants.colors import *
from App.Constants.panel import *
from App.Interface.Images.image_transformer import panel_button_img


class PanelButton:
    def __init__(self, screen, x, y, img):
        self.screen = screen
        self.rect = pygame.Rect(x, y, PANEL_BUTTON_WIDTH, PANEL_BUTTON_HEIGHT)

        self.color = LIGHT_BROWN
        self.hover_color = SUPER_LIGHT_BROWN

        self.active = False

        self.img = panel_button_img(img)

    def draw(self, mouse_pos, button_clicked):
        collides = self.rect.collidepoint(mouse_pos)
        clicked = collides and button_clicked
        
        self.active = not self.active if clicked else self.active
        color = self.hover_color if collides else self.color
            
        pygame.draw.rect(self.screen, color, self.rect)
        if self.active:
            pygame.draw.rect(self.screen, RED, self.rect, 2)
        self.screen.blit(self.img, self.rect)


        return clicked