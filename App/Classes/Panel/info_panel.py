import pygame
from App.Constants.colors import *
from App.Constants.panel import *

class InfoPanel:
    def __init__(self, screen):
        self.screen = screen
        self.active = False
        self.selected_building = None
        self.is_storage = False
        self.init_panel_rect()

        self.clicked_button = None 
        self.button_width = 60
        self.button_height = 30
        self.buttons = {
            "Iron": pygame.Rect(self.rect.x + 10, self.rect.bottom - 50, self.button_width, self.button_height),
            "Wood": pygame.Rect(self.rect.x + 90, self.rect.bottom - 50, self.button_width, self.button_height),
            "Food": pygame.Rect(self.rect.x + 170, self.rect.bottom - 50, self.button_width, self.button_height),
        }

    def init_panel_rect(self):
        screen_width, _ = self.screen.get_size()
        self.panel_width = 250  
        self.panel_height = 180  
        self.rect = pygame.Rect(screen_width - self.panel_width - 20, 20, self.panel_width, self.panel_height)

    def set_building(self, building, is_storage):
        self.selected_building = building
        self.is_storage = is_storage
        if is_storage:
            self.clicked_button = building.material.name
        self.active = building is not None

    def draw(self, mouse_pos, is_click):
        if not self.active or not self.selected_building:
            return
        
        if is_click:
            self.handle_click(mouse_pos)

        # Draw the background of the panel
        pygame.draw.rect(self.screen, (200, 173, 127), self.rect)  # Light brown color
        
        # Draw a thicker border
        pygame.draw.rect(self.screen, BLACK, self.rect, 3)

        # Set up the fonts
        title_font = pygame.font.Font(None, 32)
        font = pygame.font.Font(None, 24)

        # Building title
        building_type = self.selected_building.__class__.__name__
        title = title_font.render(building_type, True, BLACK)
        title_rect = title.get_rect(centerx=self.rect.centerx, top=self.rect.top + 15)
        self.screen.blit(title, title_rect)

        pygame.draw.line(self.screen, BLACK, 
                         (self.rect.x + 20, title_rect.bottom + 10),
                         (self.rect.right - 20, title_rect.bottom + 10), 2)

        y_offset = title_rect.bottom + 30
        
        pos_text = font.render(f"Position: ({self.selected_building.i}, {self.selected_building.j})", True, BLACK)
        self.screen.blit(pos_text, (self.rect.x + 20, y_offset))
        
        dim_text = font.render(f"Size: {self.selected_building.width}x{self.selected_building.height}", True, BLACK)
        self.screen.blit(dim_text, (self.rect.x + 20, y_offset + 35))

        if self.is_storage:
            for label, button_rect in self.buttons.items():
                if self.clicked_button == label:
                    pygame.draw.rect(self.screen, RED, button_rect)
                elif button_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.screen, GRAY, button_rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, button_rect)

                button_text = font.render(label, True, BLACK)
                text_rect = button_text.get_rect(center=button_rect.center)
                self.screen.blit(button_text, text_rect)
        else:
            pygame.draw.line(self.screen, BLACK, 
                            (self.rect.x + 20, self.rect.bottom - 25),
                            (self.rect.right - 20, self.rect.bottom - 25), 2)

    def handle_click(self, mouse_pos):
        if self.is_storage: 
            if self.selected_building.material.cant == 0:
                for label, button_rect in self.buttons.items():
                    if button_rect.collidepoint(mouse_pos):
                        self.clicked_button = label 
                        self.selected_building.assign_material(label)

                        return  

