import pygame

from App.Classes.Panel.Buttons.rotate import Rotate_Button
from App.Constants.colors import BROWN
from App.Constants.panel import PANEL_HEIGHT, PANEL_WIDTH


class RotationPanel:
    def __init__(self, screen):
        self.screen = screen
        self.active = False

        self.panel_rect()

        self.rotation_btn = Rotate_Button(screen, self.rect.x+5, self.rect.y+5)

    def panel_rect(self):
        screen_width, screen_height = self.screen.get_size()
        self.rect = pygame.Rect(0, screen_height - PANEL_HEIGHT*3, PANEL_WIDTH, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def mouse_in_panel(self, mouse_pos):
        mouse_in_rotation = self.rect.collidepoint(mouse_pos)

        return mouse_in_rotation

    def draw(self, mouse_pos, button_clicked, factory):
        if self.active:
            pygame.draw.rect(self.screen, BROWN, self.rect)
            self.rotation_btn.draw(mouse_pos, button_clicked, factory)