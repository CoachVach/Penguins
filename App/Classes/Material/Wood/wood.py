from App.Classes.Material.material import Material

class Wood(Material):
    def __init__(self, cant):
        super().__init__("Wood", cant)

    def copy(self, cant):
        return Wood(cant)