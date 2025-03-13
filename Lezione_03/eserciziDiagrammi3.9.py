'''9 . Conteggio dei numeri divisibili

Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n. Se n è negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

    l’utente può inserire 10 numeri interi;
    contare quanti di questi numeri sono divisibili per n.

Mostrare in output il risultato del conteggio.'''
while True:
    n : int = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break
    else:
        print("n deve essere positivo")
        exit()
cont = 0
for i in range(10):
    x: int = int(input("Inserisci un numero intero: "))
    if x % n == 0:
        cont += 1
print(f"I numeri divisibli per {n} sono {cont}")
