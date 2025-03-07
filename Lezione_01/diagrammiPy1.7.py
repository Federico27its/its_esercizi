'''7. Conta i numeri pari e dispari

Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.'''

pari: int = 0
dispari: int = 0
for _ in range(10):
    n: int = int(input("Inserisci un numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1

print(f"Dei 10 numeri inseriti, {pari} sono pari e {dispari} sono dispari")