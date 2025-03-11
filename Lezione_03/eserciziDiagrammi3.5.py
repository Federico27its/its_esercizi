'''5. Calcolo della somma dei quadrati fino a un numero intero positivo n

Progettare un algoritmo che, dato un numero intero positivo n definito dall'utente, calcoli la somma:

12 + 22 + 32 + 42 + 52 + ... + n2,

mostrando in output il risultato. Se n è negativo, l'algoritmo mostra un messaggio di errore e termina. '''

n: int = int(input())

if n % 1 == 0 and n > 0:
    sum = 0
    i = 1
    while i < n:
        sum += i*i
        i += 1
    print(sum)
else:
    print("Errore, n deve essere positivo")
