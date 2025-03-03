'''5. Verifica se un numero è primo

Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo.'''

n: int = int(input("Inserisci un numero intero positivo: "))

if n < 2:
    print(f"Il numero {n} non è primo...")
else:

    div: int = 2
    primo = True

    while div < n:
        if n % div == 0:
            primo = False
            break
        div += 1
if primo:
    print(f"Il numero {n} è primo...")
else:
    print(f"Il numero {n} non è primo...")




n: int = int(input("Inserisci un numero intero positivo: "))

if n < 2:
    print(f"Il numero {n} non è primo...")
else:

    primo = True
    div: int = 2

    while div < n**0.5:
        if n % div == 0:
            primo = False
            break
        div += 1

if primo:
    print(f"Il numero {n} è primo...")
else:
    print(f"Il numero {n} non è primo...")