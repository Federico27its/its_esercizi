'''8. Determinare la somma dei numero dentro un intervallo

Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.'''

A :float = float(input("Inserisci un valore A intero positiovo: "))
B: float = float(input("Inserisci un valore B intero positivo maggiore di A: "))
if A < B:
    if A > 0 and B > 0:
        if A % 1 == 0 and B %1 == 0:
            sum = 0
            i = A
            while i <= B:
                sum += i
                i += 1
            print(int(sum))
        else:
            print("A e B devono essere interi")
    else:
        print("A e B devono essere positivi")
else:
    print("A deve essere minore di B")