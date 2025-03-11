'''8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. '''
from typing import Any
def make_car(manufacter:str, model:str, **kwargs) -> dict[str: Any]:
    d: dict[str:Any] = {"manufacter" : manufacter, "model" : model}
    for key, value in kwargs.items():
        d[key] = value
    return d

print(make_car('subaru', 'outback', color='blue', two_package=True))