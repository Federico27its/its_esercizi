'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.'''

from esercizio9_1 import Restaurant

r1: Restaurant = Restaurant("Da Gigione", "giapponese")
r2: Restaurant = Restaurant("Da Paolone", "cinese")
r3: Restaurant = Restaurant("Da Sergione", "vietnamita")
r1.describe_redtaurant()
r2.describe_redtaurant()
r3.describe_redtaurant()