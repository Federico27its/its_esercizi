'''Esercizio 10.

Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".'''

def charDuplicator(s):
    if len(s) == 1:
        return s*2
    return s[0]*2 + charDuplicator(s[1:])