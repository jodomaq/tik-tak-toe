#by jodomaq
from random import randrange

#Tik Tak Toe
def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    return 0
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

def position(num):
    if num == 1:
        return (0,0)
    if num == 2:
        return (0,1)
    if num == 3:
        return (0,2)
    if num == 4:
        return (1,0)
    if num == 5:
        return (1,1)
    if num == 6:
        return (1,2)
    if num == 7:
        return (2,0)
    if num == 8:
        return (2,1)
    if num == 9:
        return (2,2)


def EnterMove(board):
    while True:
        try:    
            mov = int(input("Select a board's position: "))
            vacios = MakeListOfFreeFields(board)
            #print(vacios)
            if position(mov) in vacios:
                x = position(mov)[0]
                y = position(mov)[1]
                board[x][y] = "O"
                break
            else:
                print("Wrong position, select another.")
                continue
        except e as Exception:
            print("Input a number from 1 to 9", e)
            continue
    return 0
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

def MakeListOfFreeFields(board):
    lista = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == "X" or board[x][y] == "O":
                continue
            else:
                lista.append((x,y))
    return lista
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

def VictoryFor(board, sign):
    if board[0][0] == sign and board[0][1] == sign and board [0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board [1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board [2][2] == sign:
        return True
    if board[0][0] == sign and board[1][0] == sign and board [2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board [2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board [2][2] == sign:
        return True
    if board[0][0] == sign and board[1][1] == sign and board [2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board [2][0] == sign:
        return True
    return False
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

def DrawMove(board):
    while True:
        try:    
            mov = randrange(1,9,1)
            vacios = MakeListOfFreeFields(board)
            #print(vacios)
            if position(mov) in vacios:
                x = position(mov)[0]
                y = position(mov)[1]
                board[x][y] = "X"
                break
            else:
                continue
        except e as Exception:
            print("Unknown error:", e)
            break
    return 0
    # La función realiza el movimiento de la máquina y actualiza el tablero.

global board
board = [["1","2","3"],["4","X","6"],["7","8","9"]]
#print(board)
juega_jugador = True

while True:
    DisplayBoard(board)
    if juega_jugador:
        EnterMove(board)
        juega_jugador = False
        if VictoryFor(board,"O"):
            DisplayBoard(board)
            print("You win! :)")
            break
    else:
        DrawMove(board)
        juega_jugador = True
        if VictoryFor(board,"X"):
            DisplayBoard(board)
            print("Defeat :(")
            break
    DisplayBoard(board)
