'''11. Sistema di prenotazione di posti

Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". Per ogni opzione:

    se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
    se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
    se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.

Torna all'inserimento di una opzione finché l'utente non seleziona "esci".'''

liberi: int = 20
while True:

    opzione: str = input('Seleziona un comando tra "prenota", "libera", "visualizza" ed "esci": ')

    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -=1
            else:
                print("Non ci sono posti liberi")
        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print(f"Ci sono {liberi} posti liberi e {20 - liberi} posti occupati")
        case "esci":
            break
        case _:
            print(f"Errore: comando non riconosciuto")