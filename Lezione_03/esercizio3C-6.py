'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di
inserire il nome di un animale ed un habitat.
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci,
oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type.
Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]
habitsats: list[str] = ["acqua", "aria", "terra"]

animale: str = input("Digita il nome di un animale: ")
habitat: str = input(f"Digita l'habitat in cui vive l'animale {animale}: ")

match animale:
    case x if x in mammiferi:
        print(f"{x.title()} appartiene alla categoria dei Mammiferi")
        animal_type: str = "mammiferi"
    case x if x in rettili:
        print(f"{x.title()} appartiene alla categoria dei Rettili")
        animal_type: str = "rettili"
    case x if x in uccelli:
        print(f"{x.title()} appartiene alla categoria degli Uccelli")
        animal_type: str = "uccelli"
    case x if x in pesci:
        print(f"{x.title()} appartiene alla categoria dei Pesci")
        animal_type: str = "pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        animal_type: str ="unknown"
    
info_animale: dict = {"animale" : animale, "categoria" : animal_type, "habitat": habitat}


match info_animale:
    case {"habitat" : "terra"}:
        match info_animale["animale"]:
            case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "tartaruga", "coccodrillo", "gallina" ]:
                print(f"L'animale {animale} è uno dei {info_animale['categoria']} che puo vivere sulla terra!")
            case animale if animale in mammiferi+rettili+uccelli+pesci:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat terra")
            case _:
                print(f"Non sono in grado di fornire informazioni sull'habitat {info_animale['habitat']}")
            
    case {"habitat" : "acqua"}:
        match info_animale["animale"]:
            case animale if animale in ["serpente", "tartaruga", "coccodrillo", "squalo", "trota", "salmone", "carpa", "cigno", "anatra",  "delfino", "balena"]:
                print(f"L'animale {animale} è uno dei {info_animale['categoria']} che puo vivere in acqua!")
            case animale if animale in mammiferi+rettili+uccelli+pesci:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat acqua")
            case _:
                print(f"Non sono in grado di fornire informazioni sull'habitat {info_animale['habitat']}")

    case {"habitat" : "aria"}:
        match info_animale["animale"]:
            case animale if animale in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
                print(f"L'animale {animale} è uno dei {info_animale['categoria']} che puo vivere in aria!")
            case animale if animale in mammiferi+rettili+uccelli+pesci:
                print(f"Non ho mai visto l'animale {animale} vivere sull'habitat aria")
            case _:
                print(f"Non sono in grado di fornire informazioni sull'habitat {info_animale['habitat']}")
    
    case _:
        print(f"Non sono in grado di fornire informazioni sull'habitat {info_animale['habitat']}")