'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
 a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.'''

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_redtaurant(self):
        print(f"restaurant name: {self.name}\ncuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("the restaurant is opened :D :D :D")

r: Restaurant = Restaurant("Da Gigione", "giapponese")
print(r.name, r.cuisine_type)
r.describe_redtaurant()