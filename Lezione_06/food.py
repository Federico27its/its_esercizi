'''xercise 4 (Folder 9 ex_4.py)
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu'''

class Food:

    def __init__(self, name: str, price: float, description:str) -> None:
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, food_list: list[Food] = []) -> None:
        self.food_list = food_list
    
    def addFood(self, food: Food) -> None:
        self.food_list.append(food)

    def removeFood(self, food:Food) -> None:
        if food in self.food_list:
            self.food_list.remove(food)

    def printPrices(self) -> None:
        for food in self.food_list:
            print(f"{food.name} : {food.price}€")

    def getAveragePrice(self) -> float:
        media: float = 0.0
        for food in self.food_list:
            media += food.price
        return media/len(self.food_list)


pizza: Food = Food("pizza", 7.50, "buona")
supplì: Food = Food("supplì", 3.0, "fritto")
insalata: Food = Food("insalata", 4.50, "leggera")

menu: Menu = Menu()
menu.addFood(pizza)
menu.addFood(insalata)
menu.printPrices()
print(menu.getAveragePrice())