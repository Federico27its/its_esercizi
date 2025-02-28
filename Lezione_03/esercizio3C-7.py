'''Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%'''

t_counter: int = 0
c_counter: int = 0
c: int = 0

while c < 8:
    lancio: str = input(f"Lancio {c+1}: ").lower()
    match lancio:
        case "t":
            t_counter += 1
        case "c":
            c_counter += 1
        case _:
            print("Valore non valido...")
            c -= 1
    c += 1

print(f"Totale \"testa\": {t_counter}")
print(f"Percentuale \"testa\": {t_counter/8*100:.2f}%\n")

print(f"Totale \"croce\": {c_counter}")
print(f"Percentuale \"croce\": {c_counter/8*100:.2f}%")