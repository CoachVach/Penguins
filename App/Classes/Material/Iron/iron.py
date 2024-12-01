from App.Classes.Material.material import Material

class Iron(Material):
    def __init__(self, cant):
        super().__init__("Iron", cant)

    def copy(self, cant):
        return Iron(cant)