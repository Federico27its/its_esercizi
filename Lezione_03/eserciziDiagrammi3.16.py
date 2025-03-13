'''16. Filtrare e classificare i numeri

Progettare un algoritmo che consenta all’utente di inserire 10 numeri interi.
L'algoritmo deve:

    contare quanti numeri sono positivi e quanti sono negativi,
    verificare quanti numeri positivi sono pari e maggiori di 20,
    verificare quanti numeri negativi sono dispari o minori di -10.

Mostrare in output i conteggi distinti per ogni categoria.

Soluzione:'''

dispari :int = 0
pari: int = 0
negativi: int = 0
positivi: int = 0
for i in range(10):
    while True:
        n : float = float(input("Inserisci un numero intero diverso da 0: "))
        if n % 1 == 0 and n != 0:
            break
    if n > 0:
        positivi += 1
        if n % 2 == 0 and n > 20:
            pari += 1

    else:
        negativi += 1
        if n % 2 != 0 or n < -10:
            dispari += 1
print(positivi, negativi, pari, dispari)