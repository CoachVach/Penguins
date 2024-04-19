from App.Classes.Panel.Buttons.button import PanelButton
from App.Constants.panel import BUILD_BUTTON_IMG

class MainPanelButton(PanelButton):
    def __init__(self, screen, x, y, panel, img):
        super().__init__(screen, x, y, img)
        self.panel = panel

    def draw(self, mouse_pos, button_clicked):
        if super().draw(mouse_pos, button_clicked):
            self.panel.activate(self.active)
