'''9. Classifica delle vendite

Progetta un algoritmo che forniti dall'utente 20 totali di vendita e 
i nomi dei venditori,
 trova i due nomi dei venditori con il totale più alto e 
 il totale più basso delle vendite.'''

nome: str = input("Inserisci il nome del venditore: ")
vendite: int = int(input(f"Inserisci il numero di vendite di {nome}: "))
max: int = vendite
min_nome: str = nome
min: int = vendite

for _ in range(19):

    new_nome: str = input("Inserisci il nome del venditore: ")
    new_vendite: int = int(input(f"Inserisci il numero di vendite di {new_nome}: "))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    else:
        if new_vendite < min:
            min_nome = new_nome
            min = new_vendite

print(f"Il venditore più potente è {max_nome}, ha totalizzato {max} vendite")
print(f"Il venditore più scarso è {min_nome}, ha totalizzato {min} vendite")