import pygame
from App.Classes.Panel.Buttons.building import BuildingButton
from App.Classes.Panel.rotation import RotationPanel
from App.Constants.colors import *
from App.Constants.panel import *

class PlantPanel:
    def __init__(self, screen, builder):
        self.screen = screen
        self.active = False

        self.builder = builder

        self.init_plant_btns()

    def activate(self, active):
        self.active = active
        self.builder.activate(active)
        if active == False:
            self.deactivate_all()
            self.builder.selected = None

    def init_plant_btns(self):
        self.plant_btns = []
        self.init_panel_rect()
        i=0

        for plant in self.builder.plants:
            self.plant_btns.append(BuildingButton(self.screen, 5 + self.rect.x + (PANEL_BUTTON_WIDTH+10)*i, self.rect.y+5, plant))
            i += 1

    def init_panel_rect(self):
        screen_width, screen_height = self.screen.get_size()

        amount = len(self.builder.plants)
        self.y = screen_height - PANEL_HEIGHT*2
        rect_w = (PANEL_BUTTON_WIDTH + 10) * amount

        self.rect = pygame.Rect(0, self.y, rect_w, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def mouse_in_panel(self, mouse_pos):
        mouse_in_plants = self.rect.collidepoint(mouse_pos)

        return mouse_in_plants

    def deactivate_all(self):
        for btn in self.plant_btns:
            btn.active = False

    def draw(self, mouse_pos, button_clicked):
        if self.active:
            pygame.draw.rect(self.screen, BROWN, self.rect)
            for btn in self.plant_btns:
                if btn.draw(mouse_pos, button_clicked):
                    if btn.active:
                        self.deactivate_all()
                        btn.active = True                    
                        self.builder.selected = btn.factory
                    else:
                        self.builder.selected = None

