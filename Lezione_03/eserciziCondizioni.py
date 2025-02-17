'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''

animal : str = "cat"

print("Is animal == \"cat\"? I predict True.")
print(animal=="cat")
print("\nIs animal == \"dog\"? I predict False.")
print(animal=="dog")

print("\nIs type(animal) == str? I predict True.")
print(type(animal) == str)
print("\nIs type(animal) == int? I predict False.")
print(type(animal) == int)

print("\nIs len(animal) == 3? I predict True.")
print(len(animal) == 3)
print("\nIs len(animal) == 300000? I predict False.")
print(len(animal) == 300000)

print("\nIs animal[0] == \"c\"? I predict True")
print(animal[0]=="c")
print("\nIs animal[0] == \"ç\"? I predict False")
print(animal[0]=="ç")

print("\nIs animal[-1] == \"t\"? I predict True")
print(animal[-1]=="t")
print("\nIs animal[-1] == \"£\"? I predict False")
print(animal[-1]=="£")

print("\nIs animal[::-1] == \"tac\"? I predict True")
print(animal[::-1]=="tac")
print("\nIs animal[::-1] == \"Antonio\"? I predict False")
print(animal[::-1]=="Antonio")

'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

print("\nIs animal != \"dog\"? I predict True.")
print(animal!="dog")
print("\nIs animal != \"cat\"? I predict False.")
print(animal!="cat")

print("\nIs animal.lower() == animal? I predict True.")
print(animal.lower() == animal)
print("\nIs animal.lower() == \"CAT\"? I predict False.")
print(animal.lower() == "CAT")

print("\nIs len(animal) <= 23567235? I predict True.")
print(len(animal) <= 23567235)
print("\nIs len(animal) >= 23567235? I predict False.")
print(len(animal) >= 23567235)

print("\nIs animal == \"cat\" and len(animal) == 3? I predict True.")
print(animal == "cat" and len(animal) == 3)
print("\nIs animal == \"cat\" and len(animal) == 48954? I predict False.")
print(animal == "cat" and len(animal) == 48954)

animals : list = [animal, "dog", "bear"]
print("\nIs \"cat\" in animals? I predict True.")
print("cat" in animals)
print("\nIs \"Paolo\" in animals? I predict False.")
print("Paolo" in animals)

print("\nIs \"cat\" in animals? I predict True.")
print("cat" in animals)
print("\nIs \"Paolo\" in animals? I predict False.")
print("Paolo" in animals)

print("\nIs \"Giulio\" not in animals? I predict True.")
print("Giulio" not in animals)
print("\nIs \"bear\" in animals? I predict False.")
print("bear" not in animals)


'''5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. 
If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

alien_color : str = "green"

if alien_color == "green":
    print("You just earned 5 points")
    
alien_color : str = "red"

if alien_color == "green":
    print("You just earned 5 points")
    
'''5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.'''

alien_color : str = "green"

if alien_color == "green":
    print("You just earned 5 points")
else:
    print("You just earned 10 points")
    
alien_color : str = "red"

if alien_color == "green":
    print("You just earned 5 points")
else:
    print("You just earned 10 points")
    
'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_color : str = "green"

if alien_color == "green":
    print("You just earned 5 points")
elif alien_color == "yellow":
    print("You just earned 10 points")
elif alien_color == "red":
    print("You just earned 15 points")

alien_color : str = "yellow"

if alien_color == "green":
    print("You just earned 5 points")
elif alien_color == "yellow":
    print("You just earned 10 points")
elif alien_color == "red":
    print("You just earned 15 points")
    
alien_color : str = "red"

if alien_color == "green":
    print("You just earned 5 points")
elif alien_color == "yellow":
    print("You just earned 10 points")
elif alien_color == "red":
    print("You just earned 15 points")
    
'''5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.'''

age : int = 29

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
    
'''5-7. Favorite Fruit: Make a list of your favorite fruits,
and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list.
If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''

favorite_fruits : list = ["banana", "apple", "orange"]

if "banana" in favorite_fruits:
    print("You really like babanas!!!")
if "pinapple" in favorite_fruits:
    print("You really like pinapples!!!")
if "apple" in favorite_fruits:
    print("You really like pples!!!")
if "orange" in favorite_fruits:
    print("You really like oranges!!!")
if "kiwi" in favorite_fruits:
    print("You really like kiwis!!!")
    
'''5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''

usernames : list = ["admin", "peppone123", "peppino456", "peppe789", "giuseppe"]

for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

i: int = 0
while i < len(usernames):
    if usernames[i] == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {usernames[i]} thank you for logging in again.")
    i += 1
    
'''5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.'''
for i in range(len(usernames)):
    usernames.pop(0)
if usernames == []:
    print("We need to find some users!")

i: int = 0
while i < len(usernames):
    usernames.pop(i)
if usernames == []:
    print("We need to find some users!")
i += 1
    
'''5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users.
Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used.
If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)'''

current_users : list = ["admin", "peppone123", "peppino456", "peppe789", "giuseppe"]
current_users_caps : list = [user.upper() for user in current_users]
current_users_lower : list = [user.lower() for user in current_users]
new_users : list = ["adnim", "peppone", "peppino123", "peppe", "giuseppe"]

for i in range(len(new_users)):
    if new_users[i] in current_users or new_users[i] in current_users_lower or new_users[i] in current_users_caps:
        print("Not available, enter a new username")
    else:
        print("The usernam is available")
i: int = 0
while i < len(new_users):
    if new_users[i] in current_users or new_users[i] in current_users_lower or new_users[i] in current_users_caps:
        print("Not available, enter a new username")
    else:
        print("The usernam is available")
    i += 0
        
'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.'''

numbers : list = [n for n in range(1,10)]
for n in numbers:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")

i: int = 0


while i < len(numbers):
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
    i += 1