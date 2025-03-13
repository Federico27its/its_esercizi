'''19. Calcolo di sequenze condizionali

Scrivere un algoritmo che calcoli il valore di una sequenza numerica basata su un valore n inserito dall’utente. La sequenza segue queste regole:

    se n è pari, calcolare la somma dei numeri da 1 a n che sono divisibili per 4;
    se n è dispari, calcolare il prodotto dei numeri dispari da 1 a n;
    se n è negativo, mostrare un messaggio di errore e terminare.

Infine, mostrare il risultato calcolato.

Soluzione:'''

while True:
    n: float = float(input("Inserisci un numero intero: "))
    if n % 1 == 0:
        break
if n > 0:
    if n % 2 == 0:
        cont: int = 4
        result: int = 0
        while cont <= n:
            result += cont
            cont += 4
        print(result)
    else:
        cont: int = 1
        result: int = 1
        while cont <= n:
            result *= cont
            cont += 2
        print(result)