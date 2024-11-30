from App.Classes.Material.material import Material

class Water(Material):
    def __init__(self, cant):
        super().__init__("Water", cant)