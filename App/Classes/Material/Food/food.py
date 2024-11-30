from App.Classes.Material.material import Material

class Food(Material):
    def __init__(self, cant):
        super().__init__("Food", cant)