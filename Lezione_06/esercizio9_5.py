'''9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.'''

class User():
    def __init__(self, first_name, last_name, age, mail, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mail = mail
        self.city = city
        self.login_attempts = 0

    def greet_user(self) -> None:
        print(f"Hello {self.first_name}!!! :D")


    def describe_user(self) -> None:
        print(f"Name : {self.first_name} {self.last_name} \nAge : {self.age} \nMail : {self.mail} \nCity : {self.city}")

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0


mauro: User = User("Mauro", "Grosso", 63, "maurogrosso@gmail.com", "Napoli")
for _ in range(345):
    mauro.increment_login_attempts()
print(mauro.login_attempts)
mauro.reset_login_attempts()
print(mauro.login_attempts)