from App.Classes.Buildings.building import Building
from App.Classes.Material.Food.food import Food
from App.Classes.Material.Iron.iron import Iron
from App.Constants.Buildings.buildings import *
from App.Classes.Material.Wood.wood import Wood

class Storage(Building):
    def __init__(self, j, i, width, height, img, door_j, door_i, horizontal=True):
        super().__init__(j, i, width, height, img, door_j, door_i, horizontal)

        self.material = Wood(0) # default

        self.capacity = STORAGE_CAPACITY

    # Returns the materials left (that exceed the capacity).
    def add_element(self, material):
        if (self.material.name == material.name):
            if((self.material.cant + material.cant) <= self.capacity):
                self.material.cant += material.cant
                return None
            else:
                added = self.capacity - self.material.cant
                self.material.cant = self.capacity
                material.cant -= added
                return material
            
        return material

    def assign_material(self, material):
        if material == "Food":   
            self.material = Food(0)
        elif material == "Iron":   
            self.material = Iron(0)
        else:
            self.material = Wood(0)