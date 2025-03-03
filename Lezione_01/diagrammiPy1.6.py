'''6. Calcolo del fattoriale di un numero

Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.'''

while True:
    n: int = int(input("Inserisci un numero intero positivo: "))
    if n < 0:
        print("Il numero inserito deve essere positivo")
    else:
        break

fattoriale: int = 1
i : int = 1
while i !=  n+1:
    fattoriale *= i
    i += 1
print(f"{n} fattoriale è uguale a: {fattoriale}")
