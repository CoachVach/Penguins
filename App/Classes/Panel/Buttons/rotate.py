
from App.Classes.Panel.Buttons.button import PanelButton
from App.Constants.orientation import HORIZONTAL, VERTICAL
from App.Constants.panel import ROTATE_BUTTON_IMG


class Rotate_Button(PanelButton):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, ROTATE_BUTTON_IMG)

    def draw(self, mouse_pos, button_clicked, factory):
        if super().draw(mouse_pos, button_clicked):
            factory.rotate()
            
        self.active = factory.orientation == VERTICAL