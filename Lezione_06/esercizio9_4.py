'''9-4. Number Served: Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_redtaurant(self) -> None:
        print(f"restaurant name: {self.name}\ncuisine type: {self.cuisine_type}")

    def open_restaurant(self) -> None:
        print("the restaurant is open :D :D :D")

    def set_number_served(self, n : int) -> None:
        self.number_served = n

    def increment_number_served(self, n: int) -> None:
        self.number_served += n

r: Restaurant = Restaurant("Da Gigione", "giapponese")
print(r.number_served)
r.set_number_served(10)
print(r.number_served)
r.increment_number_served(50)
print(r.number_served)