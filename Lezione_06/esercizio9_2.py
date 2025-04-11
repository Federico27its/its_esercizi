'''9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_redtaurant(self):
        print(f"restaurant name: {self.name}\ncuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("the restaurant is opened :D :D :D")

r1: Restaurant = Restaurant("Da Gigione", "giapponese")
r2: Restaurant = Restaurant("Da Paolone", "cinese")
r3: Restaurant = Restaurant("Da Sergione", "vietnamita")
r1.describe_redtaurant()
r2.describe_redtaurant()
r3.describe_redtaurant()