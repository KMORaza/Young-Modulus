import math
class Material:
    def __init__(self, name, length, diameter):
        self.name = name
        self.length = length 
        self.diameter = diameter 
    def cross_sectional_area(self):
        radius = self.diameter / 2.0
        return math.pi * radius ** 2
    def __str__(self):
        return f"Material: {self.name}, Length: {self.length}, Diameter: {self.diameter}"
