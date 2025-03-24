class Persona:

    def __init__(self, name: str, lastname: str, age: int) -> None:
        
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")