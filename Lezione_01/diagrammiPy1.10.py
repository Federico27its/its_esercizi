'''10. Distribuzione di una borsa di studio

Progettare un algoritmo che, richiesto allo studente il reddito familiare e la media dei voti, se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, altrimenti rifiuta la richiesta visualizzando il messaggio "Borsa di studio rifiutata.
(Motivo: reddito o media insufficiente)".'''

r : int = int(input("Inserisci il reddito familiare: "))
m : int = int(input("Inserisci la media dei voti: "))

if r < 20000 and m > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)")