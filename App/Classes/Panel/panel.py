import pygame

from App.Classes.Panel.Buttons.build_button import Build_Button
from App.Classes.Panel.build import BuildPanel
from App.Constants.colors import *
from App.Constants.panel import *
from App.Interface.Images.image_transformer import panel_button_img


class Panel:
    def __init__(self, screen=None, map=None):
        self.screen = screen
        self.map = map

        self.panel_rect()
        self.build_panel = BuildPanel(screen, map.builder)
        self.build_btn = Build_Button(screen, self.rect.x+5, self.rect.y+5, self.build_panel)

    def draw(self, mouse_pos, button_clicked):
        pygame.draw.rect(self.screen, BROWN, self.rect)

        self.build_btn.draw(mouse_pos, button_clicked)
        self.build_panel.draw(mouse_pos, button_clicked)

    def panel_rect(self):
        screen_width, screen_height = self.screen.get_size()
        self.rect = pygame.Rect(0, screen_height - PANEL_HEIGHT, PANEL_WIDTH, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def mouse_in_panel(self, mouse_pos):
        mouse_in_main = self.rect.collidepoint(mouse_pos)

        mouse_in_build = self.build_panel.active and self.build_panel.rect.collidepoint(mouse_pos)
        return mouse_in_main or mouse_in_build
