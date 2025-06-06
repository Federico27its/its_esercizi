'''1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.'''

def convert(t_list: list[tuple]):
    d: dict = {}
    for t in t_list:
        if t[0] in d:
            d[t[0]] += t[1]
        else:
            d[t[0]] = t[1]
    return d

lista_tuplas = [
    ("mele", 10),
    ("banane", 5),
    ("arance", 8),
    ("pere", 3),
    ("kiwi", 12),
    ("uva", 7),
    ("limoni", 4),
    ("fragole", 15),
    ("ananas", 2),
    ("ciliegie", 9),
    ("mele", 9999)
]
print(convert(lista_tuplas))