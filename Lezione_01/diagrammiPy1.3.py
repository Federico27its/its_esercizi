'''3. Calcolo della somma di numeri positivi

Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente.
Quindi, se un numero è negativo o zero, ignora quel valore nella somma.'''

sum: float = 0
count: int = 0

while True:
    n: float = float(input("Inserisci un valore: "))
    if n > 0:
        sum += n
    count += 1
    if count == 5:
        break
print(f"La somma dei valori positivi è uguale a: {sum}")
