'''1. Calcolo cateto di un triangolo rettangolo:

Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''

a: float = float(input("Inserisci un valore a: "))
b: float = float(input("Inserisci un valore b: "))
if a > b:
    c = (a*a - b*b)**0.5
    print(f"Il valore c è uguale a: {c}")
else: 
    print("Errore")