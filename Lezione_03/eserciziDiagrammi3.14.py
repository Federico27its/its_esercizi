'''14. Simulazione di un gioco di dadi

Progettare un algoritmo che simuli un gioco basato sul lancio di due dadi virtuali a sei facce, D1 e D2. L'algoritmo deve eseguire le seguenti operazioni:

    Simulare il lancio dei due dadi.
    Calcolare la somma dei valori ottenuti dai due dadi.
    Applicare le seguenti regole di gioco per determinare il punteggio:
        Se entrambi i dadi mostrano numeri pari e la somma è maggiore di 8, il giocatore vince e il punteggio è impostato direttamente a 100.
        Se uno dei dadi mostra 6 oppure la somma è uguale a 7, il punteggio del giocatore viene incrementato di 10.
        In tutti gli altri casi, il giocatore perde e il punteggio è impostato a 0.
    Mostrare il risultato del gioco e il punteggio ottenuto.

Il gioco continua finché il punteggio totale del giocatore non raggiunge 100 (vittoria) oppure scende a zero (sconfitta).'''
'''punteggio:int = 0
while punteggio < 100:
    while True:
        d_1:int = int(input("Inserisci un valore tra 1 e 6: "))
        d_2:int = int(input("Inserisci un valore tra 1 e 6: "))
        if d_1 > 0 and d_1 <= 6 and d_2 > 0 and d_2 <= 6:
            break
    sum = d_1 + d_2
    if d_1 % 2 == 0 and d_2 % 2 == 0 and sum > 8:
        punteggio = 100
    elif d_1 == 6 or d_2 == 6 or sum == 7:
        punteggio += 10
    else:
        punteggio = 0
        print("Sconfitta")
        quit()
print("Vittoria")'''


punteggio: int = 0
while True:
    while True:
        D1: int = int(input("Inserisci un valore tra 1 e 6 "))
        D2: int = int(input("Inserisci un valore da 1 e 6 "))
        if D1 > 0 and D1 < 7 and D2 > 0 and D2 < 7:
            break
    sum = D1 + D2
    if D1 % 2 == 0 and D2 % 2 == 0 and sum > 8:
        punteggio = 100
    elif D1 == 6 or D2 == 6 or sum == 7:
        punteggio += 10
    else:
        punteggio = 0
    if punteggio >= 100 or punteggio == 0:
        break
if punteggio >= 100:
    print("Vittoria")
else:
    print("Sconfitta")
    


