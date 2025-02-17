'''4-1. Pizzas: Think of at least three kinds of your favorite pizza.
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza.
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence,
such as I really love pizza!'''

pizzas : list = ["margherita", "diavola", "marinara"]

for pizza in pizzas:
    print(f"My favorite pizza is the {pizza}")


i: int = 0
while i < len(pizzas):
    print(f"My favorite pizza is the {pizzas[i]}")
    i +=1

    
print("I REALLY LOVE PIZZA")

'''4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common.
You could print a sentence, such as Any of these animals would make a great pet!'''

animals : list = ["cat", "dog", "bear"]

for animal in animals:
    print(f"The {animal} is man's best friend")

i: int = 0
while i < len(animals):
        print(f"The {animals[i]} is man's best friend")
        i += 1

print("Any of these animals has 4 legs")

'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.'''

for i in range(1, 21):
    print(i)

i: int = 1
while i < 21:
    print(i)
    i += 1
    
'''4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)'''

# lentissimo ma funziona
'''one_million : list = []
for i in range(1,1000001):
    one_million.append(i)
for i in one_million:
    print(i)

one_million : list = []
i: int = 1
while i < 10000001:
    one_million.append(i)
    i += 1

i: int = 1
while i < len(one_million):
    print(one_million[i])
    i += 1
one_million : list = []'''


'''4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and ends at one million.
Also, use the sum() function to see how quickly Python can add a million numbers.'''
one_million : list = []
for i in range(1,1000001):
    one_million.append(i)

one_million : list = []
i: int = 1
while i < 1000001:
    one_million.append(i)
    i += 1

assert min(one_million) == 1
assert max(one_million) == 1000000
sum_million = sum(one_million)
print(sum_million)

'''4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number.'''

odds: list = []
for i in range(1, 20, 2):
    odds.append(i)
for n in odds:
    print(n)

odds: list = []
i = 1
while i < 20:
    odds.append(i)
    i += 2
i = 0
while i < len(odds):
    print(odds[i])
    i += 1

    
'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.'''

multiples : list = []
for i in range(3, 31, 3):
    multiples.append(i)
for n in multiples:
    print(n)

multiples: list = []
i = 3
while i < 31:
    multiples.append(i)
    i += 3
i = 0
while i < len(multiples):
    print(multiples[i])
    i += 1
    
'''4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.'''

cubes : list = []
for i in range(1, 11):
    cubes.append(i**3)
for n in cubes:
    print(n)

cubes: list = []
i = 1
while i <= 10:
    cubes.append(i**3)
    i += 1
i = 0
while i < len(cubes):
    print(cubes[i])
    i += 1
    
'''4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.'''

cubes: list = [n**3 for n in range(1, 11)]
# Non si può fare col while

'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''

print(f"The firs three items in the list are: {cubes[:3]}")
if len(cubes) % 2 == 0:
    print(f"Three items from the middle of the list are: {cubes[(len(cubes)//2)-2:(len(cubes)//2)+1]}")
else:
    print(f"Three items from the middle of the list are: {cubes[(len(cubes)//2)-1:(len(cubes)//2)+2]}")
print(f"The last three items in the list are: {cubes[len(cubes)-3:]}")

'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.
Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''

pizzas : list = ["margherita", "diavola", "marinara"]

friend_pizzas : list = pizzas.copy()

pizzas.append("dadi e bulloni")
friend_pizzas.append("bulloni e dadi")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My favorite pizzas are:")
i: int = 0
while i < len(pizzas):
    print(pizzas[i])
    i += 1
print("My friend's favorite pizzas are:") 
for pizza in friend_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:") 
i: int = 0
while i < len(friend_pizzas):
    print(friend_pizzas[i])
    i += 1

'''4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space.
Choose a version of foods.py, and write two for loops to print each list of foods.'''

food_list1 : list = ["pizza", "chocolate", "fries"]
food_list2 : list = ["pasta", "chicken", "rice"]

for food in food_list1:
    print(food)
for food in food_list2:
    print(food)

i: int = 0
while i < len(food_list1):
    print(food_list1[i])
    i += 1
i: int = 0
while i < len(food_list2):
    print(food_list2[i])
    i += 1

'''4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.'''

#boh mi sembrano già tutti giusti
cubes : list = []

for i in range(1, 11):
    cubes.append(i**3)
    
for n in cubes:
    print(n)

cubes: list = []
i: int = 1

while i < len(cubes):
    cubes.append(i ** 3)
    i += 1

i: int = 1

while i < len(cubes):
    print(cubes[i])
    i += 1