'''6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output.'''
'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it.'''

cities: dict = {"Rome": {"country" : "Italy", "population" : 3_000_000, "fact" : "italian capital"}, 
                "Naples": {"country" : "Italy", "population" : 1_000_000, "fact" : "italian pizza capital"}, 
                "Milan": {"country" : "Italy", "population" : 3_000_000, "fact" : "italian economic capital"}}

for key, value in cities.items():
    print(f"Here is all you need to know about the wonderfull city of {key}: ")
    for key1, value1 in value.items():
        print(f"{key1.title()} ==> {value1} :D :D :D")