'''2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.'''

def classifica_numeri(l: list):
    d = {}
    d["positivi"] = []
    d["negativi"] = []
    for n in l:
        if n > 0:
            d["positivi"].append(n)
        elif n < 0:
            d["negativi"].append(n)
    return d

print(classifica_numeri([-1, -232, 2323, -2323, 2, 4]))