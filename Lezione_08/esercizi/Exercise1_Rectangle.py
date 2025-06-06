from Exercise1_Shape import Shape

class Rectangle(Shape):
    def __init__(self, b: float, h: float):
        super().__init__()
        self.__b = b
        self.__h = h

    def area(self) -> float:
        return self.__b * self.__h
        
    def perimeter(self) -> float:
        return (self.__b + self.__h ) * 2
    
    def base(self) -> float:
        return self.__b
    
    def height(self) -> float:
        return self.__h