class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

riccardo = Person("Riccardo", 10.5)
arjol = Person("Arjol", "40")
federico = Person("Federico", 29)

persone: list = [riccardo, arjol, federico]