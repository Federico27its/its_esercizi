'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''

def prodotti_inf(d: dict):
    result = {}
    for key, value in d.items():
        if value < 50:
            result[key] = round(value + value/10, 2)

    return result
        

prodotti = {
    "t-shirt": 25.0,
    "jeans": 60.0,
    "cappello": 15.5,
    "scarpe": 80.0,
    "occhiali da sole": 45.9,
    "cintura": 35.0,
    "zaino": 49.99,
    "orologio": 120.0
}

print(prodotti_inf(prodotti))
