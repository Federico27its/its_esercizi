'''17. Sistema di gestione delle temperature

Sviluppare un algoritmo che chieda all’utente di inserire 7 temperature (una per ogni giorno della settimana). L'algoritmo deve:

    calcolare la temperatura media,
    controllare se tutte le temperature sono comprese tra 10 e 30:
        Se sì, mostrare “Temperatura nella norma”.
    verificare se almeno una temperatura è maggiore di 35 o minore di 5:
        Se sì, mostrare “Allerta temperatura”.

Mostrare in output la media, il giorno della temperatura più alta e il giorno della temperatura più bassa espresso numericamente (es. 1 per lunedì, 2 per martedì, ecc.).

Soluzione:'''

t_max: float = float("-inf")
day_max : int = 0

t_min: float = float("inf")
day_min: int = 0

cont_norma: int= 0
t_media : float = 0
i: int = 1
while i <= 7:
    temp: float = float(input("Inserisci una temperatura:"))
    t_media += temp
    if temp > t_max:
        t_max = temp
        day_max = i
    if temp < t_min:
        t_min = temp
        day_min = i
    if temp >= 10 and temp <= 30:
        cont_norma += 1
        if cont_norma == 7:
            print("Temperatura nella norma")
    elif temp < 5 or temp > 35:
        print("Allerta temperatura")
    i += 1
t_media = t_media / 7
print(t_media, t_max, t_min, day_max, day_min)