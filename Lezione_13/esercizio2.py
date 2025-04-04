'''Esercizio 2.
Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.
 '''

def compundInterest(m: float, t: int) -> float:
    return m if t == 0 else round(compundInterest(m*1.005, t-1), 2)