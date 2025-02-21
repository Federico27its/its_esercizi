'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers.'''
d1: dict = {"Jacopo" : [56, 4], "Federico" : [27, 72], "Riccardo" : [912, 918], "Sergio" : [20, 21], "Niccolò" : [12, 1, 2, 3, 4, 5, 6]}
for key, value in d1.items():
    print(f"I numeri preferiti di {key} sono: ", end = "")
    print(*value)