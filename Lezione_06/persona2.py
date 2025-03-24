class Persona:

    def __init__(self) -> None:
        
        self.name: str = ""
        self.lastname: str = ""
        self.age: int = 0

    def setName(self, name) -> None:
        self.name: str = name
    
    def setLastname(self, lastname) -> None:
        self.lastname: str = lastname
    
    def setAge(self, age) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else: 
            self.age :int = age

    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
