from App.Classes.Panel.Buttons.button import PanelButton
from App.Constants.panel import BUILD_BUTTON_IMG


class Build_Button(PanelButton):
    def __init__(self, screen, x, y, build_panel):
        super().__init__(screen, x, y, BUILD_BUTTON_IMG)
        self.build_panel = build_panel

    def draw(self, mouse_pos, button_clicked):
        if super().draw(mouse_pos, button_clicked):
            self.build_panel.activate(self.active)
