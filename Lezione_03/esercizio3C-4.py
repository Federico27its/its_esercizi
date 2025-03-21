'''Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e,
utilizzando un match statement, identifichi a quale categoria esso appartiene.
L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,
 mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

Expected Output:

Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: coccodrillo
Output: coccodrillo appartiene alla categoria dei Rettili!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: pappagallo
Output: pappagallo appartiene alla categoria degli Uccelli!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: squalo
Output: squalo appartiene alla categoria dei Pesci!
'''

mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

animale: str = input("Inserisci il nome di un animale: ")

match animale:
    case x if x in mammiferi:
        print(f"{x} appartiene alla categoria dei Mammiferi")
    case x if x in rettili:
        print(f"{x} appartiene alla categoria dei Rettili")
    case x if x in uccelli:
        print(f"{x} appartiene alla categoria degli Uccelli")
    case x if x in pesci:
        print(f"{x} appartiene alla categoria dei Pesci")
    case _:
        print("Impossibile identificare l'animale inserito")