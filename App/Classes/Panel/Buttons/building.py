from App.Classes.Panel.Buttons.button import PanelButton

class BuildingButton(PanelButton):
    def __init__(self, screen, x, y, factory):
        super().__init__(screen, x, y, factory.button_img)
        self.factory = factory