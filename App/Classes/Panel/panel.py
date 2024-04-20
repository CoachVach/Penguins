import pygame

from App.Classes.Panel.Buttons.main_button import MainPanelButton
from App.Classes.Panel.build import BuildPanel
from App.Classes.Panel.plant import PlantPanel
from App.Constants.colors import *
from App.Constants.panel import *

class Panel:
    def __init__(self, screen=None, map=None):
        self.screen = screen
        self.map = map

        self.panel_rect()

        self.build_panel = BuildPanel(screen, map.builder)
        self.build_btn = MainPanelButton(screen, self.rect.x+5, self.rect.y+5, self.build_panel, BUILD_BUTTON_IMG)

        self.plant_panel = PlantPanel(screen, map.builder)
        self.plant_btn = MainPanelButton(screen, self.rect.x + PANEL_BUTTON_WIDTH + 15, self.rect.y+5, self.plant_panel, PLANT_BUTTON_IMG)

    def draw(self, mouse_pos, button_clicked):
        pygame.draw.rect(self.screen, BROWN, self.rect)

        if self.build_btn.draw(mouse_pos, button_clicked):
            self.plant_panel.activate(False)
            self.plant_btn.active = False
        self.build_panel.draw(mouse_pos, button_clicked)

        if self.plant_btn.draw(mouse_pos, button_clicked):
            self.build_panel.activate(False)
            self.build_btn.active = False
        self.plant_panel.draw(mouse_pos, button_clicked)

    def panel_rect(self):
        screen_width, screen_height = self.screen.get_size()
        self.rect = pygame.Rect(0, screen_height - PANEL_HEIGHT, PANEL_WIDTH, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def mouse_in_panel(self, mouse_pos):
        mouse_in_main = self.rect.collidepoint(mouse_pos)

        mouse_in_build = self.build_panel.active and self.build_panel.mouse_in_panel(mouse_pos)

        mouse_in_plant = self.plant_panel.active and self.plant_panel.mouse_in_panel(mouse_pos)

        return mouse_in_main or mouse_in_build or mouse_in_plant
