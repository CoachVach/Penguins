import pygame
from App.Classes.Panel.Buttons.building import BuildingButton
from App.Constants.colors import *
from App.Constants.panel import *

class BuildPanel:
    def __init__(self, screen, builder):
        self.screen = screen
        self.active = False

        self.builder = builder

        self.init_building_btns()

    def activate(self, active):
        self.active = active
        self.builder.activate(active)
        if active == False:
            for btn in self.building_btns:
                btn.active = False

    def init_building_btns(self):
        self.building_btns = []
        self.init_panel_rect()
        i=0

        for building in self.builder.buildings:
            self.building_btns.append(BuildingButton(self.screen, 5 + self.rect.x + PANEL_BUTTON_WIDTH*i, self.rect.y+5, building.button_img))
            i += 1

    def init_panel_rect(self):
        screen_width, screen_height = self.screen.get_size()

        amount = len(self.builder.buildings)
        self.y = screen_height - PANEL_HEIGHT*2
        rect_w = (PANEL_BUTTON_WIDTH + 10) * amount

        self.rect = pygame.Rect(0, self.y, rect_w, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def draw(self, mouse_pos, button_clicked):
        if self.active:
            pygame.draw.rect(self.screen, BROWN, self.rect)
            for btn in self.building_btns:
                btn.draw(mouse_pos, button_clicked)