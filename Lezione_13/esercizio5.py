'''Esercizio 5.

Una progressione armonica è definita come il prodotto dei reciproci dei primi n numeri interi positivi, ovvero il risultato della moltiplicazione di 1 diviso ogni numero intero da 1 fino a n.
Ad esempio, se n = 6, la progressione armonica A vale:
A = 1/6 * 1/5 * 1/4 * 1/3 * 1/2 * 1 = 0.001389.

Scrivere in Python una funzione ricorsiva chiamata armonica che dato un numero n intero positivo, calcoli la relativa progressione armonica, arrotondando il risultato finale a 6 cifre decimali.
 '''

def prog(n: int) -> float:
    return 1 if n == 1 else round(1/n * prog(n-1), 6)