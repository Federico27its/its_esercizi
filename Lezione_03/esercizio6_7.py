'''6-7. People: Start with the program you wrote for Exercise 6-1.
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people.
As you loop through the list, print everything you know about each person.'''

d1: dict = {"first_name" : "Jacopo", "last_name" : "Jacopone", "age" : 50, "city" : "Rome"}
d2: dict = {"first_name" : "Sergio", "last_name" : "Sergione", "age" : 5, "city" : "Rome"}
d3: dict = {"first_name" : "Riccardo", "last_name" : "Riccardone", "age" : 55, "city" : "Rome"}
l1: list = [d1, d2, d3]
for d in l1:
    for key, value in d.items():
            print(key, value)