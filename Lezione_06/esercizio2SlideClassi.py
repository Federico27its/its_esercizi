class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self) -> None:
        print(f"{self.name}, {self.studyProgram}, {self.age}, {self.gender}")

io: Student = Student("Federico", "python", 29, "M")
riccardo: Student = Student("Riccardo", "hacking da terminale", 19, "M")
arjol: Student = Student("Arjol", "python2", 42, "M")

io.printInfo()
