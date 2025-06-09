'''3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''

def prodotti_inf(d: dict):
    result = {}
    for key, value in d.items():
        if value < 50:
            result[key] = round(value + value/10, 2)

    return result