board = [
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"]
]


def board_print(bord):
    print("     A   B   C   D   E   F   G   H")
    for i in range(len(board)):
        print(i + 1, " |", " | ".join(board[i]), "| ")
        print("  ", "-" * 33)


# "■■■■", "■■■", "■■■", "■■", "■■", "■■", "■", "■", "■", "■"]
# 1 = "■■■■", 2, 3 = "■■■" 4, 5, 6 = "■■" 7, 8 , 9, 10 = "■"
def put_ship(board):
    for j in range(1, 11):
        # "■■■■"
        if j == 1:
            print("put ■■■■ ship")
            var_aj = input("horizontal vertical? (1/2)")
            row = int(input("row(1, 2, 3, 4, 5, 6, 7, 8)"))
            column = int(input("column(A, B, C, D, E, F, G, H)"))
            if var_aj == "2":
                for i in range(1, 5):
                    board[row - i - 5][column - 1] = "■"
            elif var_aj == "1":
                for i in range(1, 5):
                    board[row - 1][column - 1:column - i - 4] = "■"
            board_print(board)
        # "■■■"
        elif j == 2 or j == 3:
            print("put ■■■ ship")
            var_aj = input("horizontal/vertical? (1/2)")
            row = int(input("row(1, 2, 3, 4, 5, 6, 7, 8)"))
            column = int(input("column(A, B, C, D, E, F, G, H)"))
            if var_aj == "2":
                for i in range(1, 4):
                    board[row - i - 6][column - 1] = "■"
            elif var_aj == "1":
                for i in range(1, 4):
                    board[row - 1][column - 1:column - i - 5] = "■"
            board_print(board)
        # "■■"
        elif j == 4 or j == 5 or j == 6:
            print("put ■■ ship")
            var_aj = input("horizontal/vertical? (1/2)")
            row = int(input("row(1, 2, 3, 4, 5, 6, 7, 8)"))
            column = int(input("column(A, B, C, D, E, F, G, H)"))
            if var_aj == "2":
                for i in range(1, 3):
                    board[row - i - 7][column - 1] = "■"
            elif var_aj == "1":
                for i in range(1, 3):
                    board[row - 1][column - 1:column - i - 6] = "■"
            board_print(board)
        # "■"
        else:
            print("put ■ ship")
            row = int(input("row(1, 2, 3, 4, 5, 6, 7, 8)"))
            column = int(input("column(A, B, C, D, E, F, G, H)"))
            board[row - 1][column - 1] = "■"
            board_print(board)
    return board


board_print(board)
a = put_ship(board)
board_print(a)






