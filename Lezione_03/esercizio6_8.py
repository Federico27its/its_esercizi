'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets.
Next, loop through your list and as you do, print everything you know about each pet. '''
p1: dict = {"kind of animal" : "dog", "owner's name" : "Jacopo", "age" : 6}
p2: dict = {"kind of animal" : "cat", "owner's name" : "Riccardo", "age" : 8}
p3: dict = {"kind of animal" : "monkey", "owner's name" : "Alessio", "age" : 10}
l1: list = [p1, p2, p3]
for d in l1:
    for key, value in d.items():
        print(key, value)