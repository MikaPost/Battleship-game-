import sys
from colorama import init, Fore, Style
init()
from boards import board_player1, board_player11, board_player2, board_player22

a1 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

def start():
    st = input("Start game? (Yes/No)")
    if st.lower() == "yes":
        return True
    else:
        print("Exiting the game.")
        sys.exit()

def board_print(board, pl):
    if pl == 1:
        i = 1
        print("    " + Fore.RED + "yours board" + "         " + "opponent's board" + Style.RESET_ALL)
        print(Fore.BLUE + "  A B C D E F G H       A B C D E F G H" + Style.RESET_ALL)
        for row1, row2 in zip(board, board_player11):
            print(Fore.YELLOW + str(i), ' '.join(row1) + "    ", i,  ' '.join(row2))
            i += 1
        print(Style.RESET_ALL)
    else:
        i = 1
        print("    " + Fore.RED + "yours board" + "         " + "opponent's board" + Style.RESET_ALL)
        print(Fore.GREEN + "  A B C D E F G H       A B C D E F G H" + Style.RESET_ALL )
        for row1, row2 in zip(board, board_player22):
            print(Fore.CYAN + str(i),  ' '.join(row1) + "    ", i, ' '.join(row2))
            i += 1
        print(Style.RESET_ALL)


def is_square_empty(board, row, column):
    return board[row][column] == "-"


def put_ship_4(board, player):
    if player == 1:
        print("First player's turn".upper())
    else:
        print("Second player's move".upper())
    print("Put ■■■■ ship")
    var_aj = input("Horizontal or Vertical? (1/2)")
    row = int(input("Row (1, 2, 3, 4, 5, 6, 7, 8): "))
    column = input("Column (A, B, C, D, E, F, G, H): ").lower()
    if var_aj == "2":
        for i in range(4):
            board[row - 1 + i][a1[column]] = "■"
    elif var_aj == "1":
        for i in range(4):
            board[row - 1][a1[column] + i] = "■"
    board_print(board, player)
    return put_ship_3(board, player)


def put_ship_3(board, player):
    def are_squares_empty(board, row, column, num_squares, is_horizontal):
        if is_horizontal:
            return all(is_square_empty(board, row, column + i) for i in range(num_squares))
        else:
            return all(is_square_empty(board, row + i, column) for i in range(num_squares))

    for j in range(2):
        print("Put ■■■ ship")
        var_aj = input("Horizontal or Vertical? (1/2)")
        row = int(input("Row (1, 2, 3, 4, 5, 6, 7, 8): ")) - 1
        column = a1[input("Column (A, B, C, D, E, F, G, H): ").lower()]
        if var_aj == "2":
            if are_squares_empty(board, row, column, 3, False):
                for i in range(3):
                    board[row + i][column] = "■"
            else:
                print("Cannot place ship here. Square is already occupied.")
                return put_ship_3(board, player)

        elif var_aj == "1":
            if are_squares_empty(board, row, column, 3, True):
                for i in range(3):
                    board[row][column + i] = "■"
            else:
                print("Cannot place ship here. Square is already occupied.")
                return put_ship_3(board, player)

        board_print(board, player)
    return put_ship_2(board, player)




def put_ship_2(board, player):
    def are_squares_empty(board, row, column, num_squares, is_horizontal):
        if is_horizontal:
            return all(is_square_empty(board, row, column + i) for i in range(num_squares))
        else:
            return all(is_square_empty(board, row + i, column) for i in range(num_squares))

    for j in range(3):
        print("Put ■■ ship")
        var_aj = input("Horizontal or Vertical? (1/2)")
        row = int(input("Row (1, 2, 3, 4, 5, 6, 7, 8): ")) - 1
        column = a1[input("Column (A, B, C, D, E, F, G, H): ").lower()]
        if var_aj == "2":
            if are_squares_empty(board, row, column, 2, False) :
                for i in range(2):
                    board[row + i][column] = "■"
            else:
                print("Cannot place ship here. Square is already occupied.")
                return put_ship_2(board, player)
        elif var_aj == "1":
            if are_squares_empty(board, row, column, 2, True):
                for i in range(2):
                    board[row][column + i] = "■"
            else:
                print("Cannot place ship here. Square is already occupied.")
                return put_ship_2(board, player)

        board_print(board, player)
    return put_ship_1(board, player)


def put_ship_1(board, player):

    for j in range(4):
        print("Put ■ ship")
        row = int(input("Row (1, 2, 3, 4, 5, 6, 7, 8): ")) - 1
        column = a1[input("Column (A, B, C, D, E, F, G, H): ").lower()]

        if is_square_empty(board, row, column):
            board[row][column] = "■"
        else:
            print("Cannot place ship here. Square is already occupied.")
            return put_ship_1(board, player)

        board_print(board, player)
    return board


def main():
    if start():
        board_print(board_player1, 1)
        put_ship_4(board_player1, 1)
        board_print(board_player1, 1)

        board_print(board_player2, 2)
        put_ship_4(board_player2, 2)
        board_print(board_player2, 2)



if __name__ == "__main__":
    main()
