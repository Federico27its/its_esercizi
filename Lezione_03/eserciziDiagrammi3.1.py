'''1. Sistema di gestione per un parcheggio
Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio con un numero massimo di posti dato in input. L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:

    se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
    se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.

Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

max_posti: int = int(input())
liberi: int = max_posti


while True:
    opzione : str = input()
    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
            else:
                print("non ci sono posti disponibili")
        case "uscita":
            if liberi < max_posti:
                liberi += 1
            else:
                print("tutti i posti sono già disponibili")
        case "stato":
            print(liberi)
            print(max_posti - liberi)
        case "esci":
            break
        case _:
            print("opzione non riconosciuta")
