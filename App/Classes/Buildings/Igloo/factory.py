from App.Classes.Factory.factory import Factory
from App.Constants.panel import IGLOO_BUTTON_IMG

class IglooFactory(Factory):
    def __init__(self):
        super().__init__(button_img = IGLOO_BUTTON_IMG)