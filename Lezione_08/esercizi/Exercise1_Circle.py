from Exercise1_Shape import Shape

import math

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.__radius = radius

    def area(self) -> float:
        return math.pow(self.__radius, 2)*math.pi
        
    def perimeter(self) -> float:
        return self.__radius * math.pi * 2
        
    def radius(self) -> float:
        return self.__radius