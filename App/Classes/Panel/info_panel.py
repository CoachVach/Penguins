import pygame
from App.Constants.colors import *
from App.Constants.panel import *

class InfoPanel:
    def __init__(self, screen):
        self.screen = screen
        self.active = False
        self.selected_building = None
        self.init_panel_rect()

    def init_panel_rect(self):
        screen_width, _ = self.screen.get_size()
        self.panel_width = 250  # Un poco más ancho
        self.panel_height = 180  # Un poco más alto
        self.rect = pygame.Rect(screen_width - self.panel_width - 20, 20, self.panel_width, self.panel_height)

    def set_building(self, building):
        self.selected_building = building
        self.active = building is not None

    def draw(self):
        if not self.active or not self.selected_building:
            return

        # Dibujar el fondo del panel con un color más claro
        pygame.draw.rect(self.screen, (200, 173, 127), self.rect)  # Marrón más claro
        
        # Dibujar un borde más grueso
        pygame.draw.rect(self.screen, BLACK, self.rect, 3)

        # Configurar la fuente
        title_font = pygame.font.Font(None, 32)
        font = pygame.font.Font(None, 28)
        
        # Título del building
        building_type = self.selected_building.__class__.__name__
        title = title_font.render(building_type, True, BLACK)
        title_rect = title.get_rect(centerx=self.rect.centerx, top=self.rect.top + 15)
        self.screen.blit(title, title_rect)

        # Línea separadora
        pygame.draw.line(self.screen, BLACK, 
                        (self.rect.x + 20, title_rect.bottom + 10),
                        (self.rect.right - 20, title_rect.bottom + 10), 2)

        # Información del building
        y_offset = title_rect.bottom + 30
        
        # Posición
        pos_text = font.render(f"Position: ({self.selected_building.i}, {self.selected_building.j})", True, BLACK)
        self.screen.blit(pos_text, (self.rect.x + 20, y_offset))
        
        # Dimensiones
        dim_text = font.render(f"Size: {self.selected_building.width}x{self.selected_building.height}", True, BLACK)
        self.screen.blit(dim_text, (self.rect.x + 20, y_offset + 35)) 