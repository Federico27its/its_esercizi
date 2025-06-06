'''Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla.
Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

Expected Output:

Inserisci la coordinata X: 0
Inserisci la coordinata Y: 0
Output: Il punto (0,0) si trova nell'origine.

- - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 3
Inserisci la coordinata Y: 5
Output: Il punto (3,5) si trova nel primo quadrante.

- - - - - - - - - - - - - - - - - - - - - - - - -

Inserisci la coordinata X: 4
Inserisci la coordinata Y: 0
Output: Il punto (4,0) si trova sull'asse X.'''

x: int = int(input("Inserisci la coordinata X: "))
y: int = int(input("Inserisci la coordinata Y: "))
point: tuple[int] = (x, y)

match point:
    case (0, 0):
        print("Il punto (0,0) si trova nell'origine.")
    case (x, 0):
        print (f"Il punto ({x},0) si trova sull'asse X.")
    case (0, y):
        print (f"Il punto (0,{y}) si trova sull'asse X.")
    case (x, y) if x > 0 and y > 0:
        print(f"Il punto ({x},{y}) si trova nel primo quadrante.")
    case (x, y) if x < 0 and y > 0:
        print(f"Il punto ({x},{y}) si trova nel secondo quadrante.")
    case (x, y) if x < 0 and y < 0:
        print(f"Il punto ({x},{y}) si trova nel terzo quadrante.")
    case (x, y) if x > 0 and y < 0:
        print(f"Il punto ({x},{y}) si trova nel primo quadrante.")