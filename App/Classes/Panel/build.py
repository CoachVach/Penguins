import pygame
from App.Classes.Panel.Buttons.building import BuildingButton
from App.Classes.Panel.rotation import RotationPanel
from App.Constants.colors import *
from App.Constants.panel import *

class BuildPanel:
    def __init__(self, screen, builder):
        self.screen = screen
        self.active = False

        self.builder = builder

        self.rotation_panel = RotationPanel(screen)

        self.init_building_btns()

    def activate(self, active):
        self.active = active
        self.builder.activate(active)
        if active == False:
            self.deactivate_all()
            self.builder.selected = None
            self.rotation_panel. active = False

    def init_building_btns(self):
        self.building_btns = []
        self.init_panel_rect()
        i=0

        for building in self.builder.buildings:
            self.building_btns.append(BuildingButton(self.screen, 5 + self.rect.x + (PANEL_BUTTON_WIDTH+10)*i, self.rect.y+5, building))
            i += 1

    def init_panel_rect(self):
        screen_width, screen_height = self.screen.get_size()

        amount = len(self.builder.buildings)
        self.y = screen_height - PANEL_HEIGHT*2
        rect_w = (PANEL_BUTTON_WIDTH + 10) * amount

        self.rect = pygame.Rect(0, self.y, rect_w, PANEL_HEIGHT)
        self.rect.centerx = screen_width // 2

    def mouse_in_panel(self, mouse_pos):
        mouse_in_build = self.rect.collidepoint(mouse_pos)

        mouse_in_rotation = self.rotation_panel.active and self.rotation_panel.mouse_in_panel(mouse_pos)

        return mouse_in_build or mouse_in_rotation

    def deactivate_all(self):
        for btn in self.building_btns:
            btn.active = False

    def draw(self, mouse_pos, button_clicked):
        if self.active:
            pygame.draw.rect(self.screen, BROWN, self.rect)
            for btn in self.building_btns:
                if btn.draw(mouse_pos, button_clicked):
                    if btn.active:
                        self.deactivate_all()
                        btn.active = True                    
                        self.builder.selected = btn.factory
                        self.rotation_panel.active = True
                    else:
                        self.builder.selected = None
                        self.rotation_panel.active = False
                        self.rotation_panel.rotation_btn.active = False

            self.rotation_panel.draw(mouse_pos, button_clicked, self.builder.selected)

