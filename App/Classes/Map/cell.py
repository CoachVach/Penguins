class Cell:
    def __init__(self):
        self.building = None
        self.x = None
        self.y = None

    def is_empty(self):
        return self.building == None

    def set_building(self, building):
        self.building = building

    def set_position(self, x, y):
        self.x = x
        self.y = y 