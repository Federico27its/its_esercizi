'''2. Trova il massimo tra 4 numeri:

Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''

max: float = float(input("Inserisci un valore: "))
for _ in range(3):
    n: float = float(input("Inserisci un valore: "))
    if n > max:
        max = n
print(f"Il valore massimo è uguale a: {max}")

max: float = float(input("Inserisci un valore: "))
c: int = 0
while c < 4:
    n: float = float(input("Inserisci un valore: "))
    if n > max:
        max = n
    c += 1
print(f"Il valore massimo è uguale a: {max}")

max: float = float(input("Inserisci un valore: "))
c: int = 1
while True:
    n: float = float(input("Inserisci un valore: "))
    if n > max:
        max = n
    c += 1
    if c == 4:
        break
print(f"Il valore massimo è uguale a: {max}")



