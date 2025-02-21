'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it.'''

cities: dict = {"Rome": {"country" : "Italy", "population" : 3_000_000, "fact" : "italian capital"}, 
                "Naples": {"country" : "Italy", "population" : 1_000_000, "fact" : "italian pizza capital"}, 
                "Milan": {"country" : "Italy", "population" : 3_000_000, "fact" : "italian economic capital"}}

for key, value in cities.items():
    print(f"{key}: ")
    for key1, value1 in value.items():
        print(key1, value1)