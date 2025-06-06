rules_board = [[y * 3 + x + 1 for x in range (3)] for y in range(3)]


def gameover(board: list[list[str]]) -> None | str:

    for x in range(len(board)):
        if " " in board[x]:
                return None
        
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        if board[0][x] == board[1][x] == board [2][x]:
            return board[0][x]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    return None

def print_board(board: list[list[str]]) -> None:
    for x in range(len(board)):
        print("+-----+-----+-----+", end = "     ")
        print("+-----+-----+-----+")

        for y in range(len(board[0])):
            match y: 
                case 0:
                    print(f"|  {board[x][y]}  ", end = "")
                case 1:
                    print(f"|  {board[x][y]}  |", end = "")
                case 2:
                    print(f"  {board[x][y]}  |", end = "     ")
        print(f"|  {rules_board[x][0]}  |  {rules_board[x][1]}  |  {rules_board[x][2]}  |")
    print("+-----+-----+-----+", end = "     ")
    print("+-----+-----+-----+")

    

def move(board: list[list[str]], p: str, pos: int):
    board[(pos-1) // 3 ][(pos % 3) - 1] = p

def get_move() -> int:
    while True:
        try:
            i = float(input("Scegli una casella:\n>>>"))
            if i == "q":
                exit
            if i.is_integer() and 1 <= i <= 9:
                return i
            else:
                print("Mossa non valida")
        except:
            print("Mossa non valida")

def new_game() -> None:
    p1: str = "X"
    p2: str = "O"
    p1_turn: str = True
    board: list[list[str]] = [[" " for x in range (3)] for y in range(3)]
    while not gameover(board):
        print_board(board)
        i = get_move()
        move(board, p1 if p1_turn else p2, int(i))
        p1_turn = not p1_turn
        #print(rules_board[0], rules_board[1], rules_board[2])
    else:
        print("Partita terminata evvai")
        print_board(board)
new_game()
