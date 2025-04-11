'''9-3. Users: Make a class called User.
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.'''

class User():
    def __init__(self, first_name, last_name, age, mail, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mail = mail
        self.city = city

    def greet_user(self):
        print(f"Hello {self.first_name}!!! :D")


    def describe_user(self):
        print(f"Name : {self.first_name} {self.last_name} \nAge : {self.age} \nMail : {self.mail} \nCity : {self.city}")


mauro: User = User("Mauro", "Grosso", 63, "maurogrosso@gmail.com", "Napoli")
patrizio: User = User("Patrizio", "Grosso", 64, "patriziogrosso@gmail.com", "Napoli")

mauro.describe_user()
mauro.greet_user()

patrizio.describe_user()
patrizio.greet_user()

