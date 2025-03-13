'''7. Algoritmo per il calcolo della media dei voti con inserimento iterativo

Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, calcolandone la media. L'algoritmo deve chiedere all'utente se vuole inserire un voto. 

Se la risposta è "SI", allora l'utente può procedere ad inserire il voto. L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 

Infine, mostrare in output il valore medio dei voti inseriti.'''

cont: int = 0
sum: int = 0
while True:
    scelta = input("Vuoi inserire un voto? ")
    if scelta == "si":
        while True:
            voto = int(input("Inserisci un voto positivo: "))
            if voto > 0:
                cont += 1
                sum += voto
                break
            else:
                print("errore")
    elif scelta == "no":
        if cont > 0:
            media = sum/cont
            print(f"La media dei voti è uguale: {media}")
        else:
            print("Nessun voto inserito")