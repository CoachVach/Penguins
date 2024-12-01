class MapBuildings():
    def __init__(self):
        self.iglooes = []
        self.barrels = []
        self.storages = []
        self.plants = []

    def all_buildings(self):
        return self.iglooes + self.barrels + self.storages + self.plants

    def buildings_in_construction(self):
        return [building for building in self.all_buildings() if not building.constructed()]
        