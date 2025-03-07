''' i numeri maggiori di un valore soglia

Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.'''

soglia: int = int(input())
cont: int = 0
while cont < 7:
    n: int = int(input())
    if n > soglia:
        print(f"{n} è maggiore di {soglia}!!!🤯")
    cont += 1