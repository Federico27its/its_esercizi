'''Esercizio 8.

Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''

def vowelsCounter(s: str) -> int:
    if len(s) == 1:
        return 1 if s in "aeiouAEIOU" else 0
    
    if s[0] in "aeiouAEIOU":
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])