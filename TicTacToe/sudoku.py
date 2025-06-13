import os


coords: list[list[int]] = [
                           [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 
                           [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], 
                           [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], 
                           [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)], 
                           [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], 
                           [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                           [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)], 
                           [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)], 
                           [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
                           ]



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def print_board(board: list[list[int]]) -> None:

    clear_console()
    print(end = "   ")
    for x in range(len(board)):
        print(f"\033[31m  {x+1} \033[0m", end = "")
    print()

    for x in range(len(board)):
        if x == 0 or x % 3 == 0:
            print(f"   {'='*37}")
        else:
            print("   ║---+---+---║---+---+---║---+---+---║")
        print(f"\033[31m {chr(x + ord('a'))}\033[0m", end = "")

        for y in range(len(board[0])):
            if y == 0:
                print(f" ║ {board[x][y]} |", end = "")
            elif y % 3 == 2:
                print(f" {board[x][y]} ║", end = "")
            else:
                print(f" {board[x][y]} |", end = "")
        print()
    print(f"   {'='*37}")



def create_board() -> list[list[str]]:

    board: list[list[str]] = [[" " for x in range (9)] for y in range(9)] # cambio prima x con " " per board vuota (ma va)
    return board



def get_coord() -> tuple[int, int]:

    while True:
        try:
            i = input("Scegli una casella\n>>>").strip()
            if " " in i:
                 i = i.replace(" ", "")
            if len(i) == 2 and "a" <= i[0] <= "i" and 1 <= int(i[1]) <= 9:
                return (ord(i[0]) - ord("a"), int(i[1]) - 1)
            else:
                print("Errore: input non valido")
        except:
            print("Errore: input non valido")



def get_value() -> int:

    while True:
        try:
            i = float(input("Scegli un numero da 0 a 9:\n>>>"))
            if i.is_integer() and 0 <= i <= 9:
                return int(i)
            else:
                print("Errore: input non valido")
        except:
            print("Errore: input non valido")



def valid_move(board: list[list[int]], coord: tuple[int, int], value: int):

    for x in range(len(coords)): # controllo nel 3x3
        if coord in coords[x]:
            for y in range(len(coords[x])):
                if value == board[coords[x][y][0]][coords[x][y][1]]:
                    return False
                
    if value in board[coord[0]]: # controllo riga
        return False
    
    for i in range(9):
        if board[i][coord[1]] == value:
            return False
        
    return True



def write_move(board: list[list[int]], coord: tuple[int, int], value: int) -> None:


    if valid_move(board, coord, value):
        if value == 0:
            value = " "
        board[coord[0]][coord[1]] = value



def game_over(board: list[list[int]]) -> bool:

    for x in range(len(board)):
        if set(board[x]) != set(1, 2, 3, 4, 5, 6, 7, 8, 9):
            return False
    return True
    


board = create_board()
print_board(board)
for _ in range(5):
    coord, value = get_coord(), get_value()
    write_move(board, coord, value)
    print_board(board)
print("basta ti sei divertito\n")
input("digita qualcosa per uscire stupido\n\n")