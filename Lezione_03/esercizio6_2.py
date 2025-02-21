'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.'''

d1: dict = {"Jacopo" : 56, "Federico" : 27, "Riccardo" : 912, "Sergio" : 20, "Niccolò" : 12}
for key, value in d1.items():
    print(f"Il numero preferito di {key} è: {value}")