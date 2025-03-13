'''

13. Esercizio di controllo numerico con condizioni arbitrarie

Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

    la somma di x+y+z deve essere pari;
    x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
    se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare: “Regole non rispettate”.
'''

while True:
    x: float = float(input("Inserisci un numero intero positivo "))
    y: float = float(input("Inserisci un numero intero positivo "))
    z: float = float(input("Inserisci un numero intero positivo "))
    if x % 1 == 0 and x > 0:
        if y % 1 == 0 and y > 0:
            if z % 1 == 0 and z > 0:
                if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
                    print("Regola rispettate")
                else:
                    print(x+y+z, x, y, z)

            else:
                print("z deve essere intero e positivo")
        else:
            print("y deve essere intero e positivo")
    else:
        print("x deve essere intero e positivo")