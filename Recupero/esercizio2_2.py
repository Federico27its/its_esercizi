
'''2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.'''

def mult(l: list, threshold: int):
    prod = 1
    for n in l:
        if n < threshold:
            prod *= n

    return prod

print(mult([1, 2, 3, 4, 5, 6], 4))


def fact_rec(n: int):
    return 1 if n == 1 else n*fact_rec(n-1)
