'''Exercise 3 (Folder 9 ex_3.py)
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''

class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self.name = name
        self.legs = legs
    
    def setLegs(self, legs: int) -> None:
        self.legs = legs
    
    def getLegs(self) -> int:
        return self.legs
    
    def printInfo(self) -> None:
        print(f"{self.name} ha {self.legs} zampe")
    
scimmia: Animal = Animal("scimmia", 4)
piccione: Animal = Animal("piccione", 2)

piccione.legs = 1
piccione.setLegs(2)

