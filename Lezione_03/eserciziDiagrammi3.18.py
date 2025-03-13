'''18. Classifica e somma condizionale

Scrivere un algoritmo che consenta all’utente di inserire una numero variabile di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

    sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
    sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;

Mostrare in output entrambe le somme e indicare quale somma è maggiore.

Soluzione:'''

while True:
    n: float = float(input("Inserisci un numero intero: "))
    if n % 1 == 0:
        break
somma:int = 0
media:float = 0
somma_pari: int = 0
somma_dispari: int = 0
for i in range(1, int(n)+1):
    while True:
        x: float = float(input("Inserisci un numero intero: "))
        if x % 1 == 0:
            break
    somma += x
    media = somma/i

    if x % 2 == 0 and x > media:
        somma_pari += x 
    elif x < media or x % 2 != 0:
        somma_dispari += x
print(somma_pari, somma_dispari)
if somma_pari > somma_dispari:
    print("somma_pari è maggiore")
elif somma_dispari > somma_pari:
    print("somma_dispari è maggiore")
else:
    print("le somme sono uguali")


        
