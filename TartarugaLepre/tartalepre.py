import random

def visualizza(percorso: list[int], tortoise:int, hare:int) -> None:

    tabellone = []

    for n in percorso:
        if n == tortoise == hare:
            tabellone += list("OUCH!!!")
        elif n == tortoise:
            tabellone.append("T")
        elif n == hare:
            tabellone.append("H")
        else:
            tabellone.append("_")

    
    if len(tabellone) > len(percorso):
        print(tabellone[len(percorso)-len(tabellone):])
    else:
        print(tabellone, "\n")

def mossa_tartaruga(tortoise: int, stamina_t: int) -> tuple[int]:
    r = random.randint(1, 10)

    if r <= 5:      #Passo veloce

        if stamina_t < 5:
            stamina_t += 10
        else:
            tortoise += 3
            stamina_t -= 5

    elif r <= 8:    #Passo lento

        if stamina_t < 3:
            stamina_t += 10
        else:
            tortoise += 1
            stamina_t -= 3

    elif r <= 10:   #Scivolata
        if stamina_t < 10:
            stamina_t += 10
        else:
            tortoise -= 6
            stamina_t -= 10
    if pioggia: tortoise -= 1

    if tortoise in bonus:
        tortoise += bonus[tortoise]

    elif tortoise in ostacoli:
        tortoise += ostacoli[tortoise]

    return min(max(tortoise, 1), 70), min(max(stamina_t, 1), 100)
    
def mossa_coniglio(hare: int, stamina_h) -> tuple[int]:
    r = random.randint(1, 10)

    if r <= 3:      #Piccolo balzo
        if stamina_h > 5:
            hare += 1
            stamina_h -= 5

    elif r <= 5:    #Grande balzo
        if stamina_h > 15:
            hare += 9
            stamina_h -= 15

    elif r <= 7:    #Riposo
        stamina_h += 10
        if pioggia: hare -= 2
        return min(max(hare, 1), 70), min(max(stamina_h, 1), 100)
    
    elif r <= 9:    #Piccola scivolata
        if stamina_h > 8:
            hare -= 2
            stamina_h -= 8

    elif r <=10:    #Grande scivolata
        if stamina_h > 15:
            hare -= 12
            stamina_h -= 15

    if pioggia: hare -= 2

    if hare in bonus:
        hare += bonus[hare]

    elif hare in ostacoli:
        hare += ostacoli[hare]

    return min(max(hare, 1), 70), min(max(stamina_h, 1), 100)


percorso: list[int] = list(range(1,71))
ostacoli: dict[int:int] = {15: -3, 30: -5, 45: -7}
bonus: dict[int:int] = {10: 5, 25: 3, 50: 10}

hare: int = 1
stamina_h: int = 100

tortoise: int = 1
stamina_t: int = 100

pioggia: bool = False

thick:int = 1

print("BANG !!!!! AND THEY'RE OFF !!!!!")

while True:

    hare, stamina_h = mossa_coniglio(hare, stamina_h)

    tortoise, stamina_t = mossa_tartaruga(tortoise, stamina_t)

    visualizza(percorso, tortoise, hare)

    if thick % 10 == 0:
        pioggia = not pioggia

    thick += 1
    
    '''print(f"Tartaruga:\nPosizione: {tortoise} | Stamina: {stamina_t}")
    print("\n")
    print(f"Coniglio:\nPosizione: {hare} | Stamina: {stamina_h}")
    print("\n")
    print(f"Meteo: Sole") if not pioggia else print(f"Meteo: Pioggia")
    print("\n")
    print(f"\nThick n.{thick}\n")'''

    if hare >= 70 and tortoise >= 70:
        print("IT'S A TIE.")
        break

    elif hare >= 70:
        print("HARE WINS || YUCH!!!")
        break

    elif tortoise >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break