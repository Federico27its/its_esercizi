# Lezione 3, diagrammi, esercizio 1
posti = int(input())
posti_occupati = 0
while True: 
    comando = input()
    if comando == "ingresso":
        if posti_occupati < posti:
            posti_occupati += 1
    elif comando == "uscita":
        if posti_occupati > 0:
            posti_occupati -= 1
    elif comando == "stato":
        print(posti - posti_occupati, posti_occupati)
    elif comando == "esci":
        break