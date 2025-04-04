'''Esercizio 9.

Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.'''

def vowelRemover(s):
    if len(s) == 1:
        if s in "aeiouAEIOU":
            return ""
        else:
            return s
    if s[0] in "aeiouAEIOU":
        return vowelRemover(s[1:])
    else:
        return s[0] + vowelRemover(s[1:])
