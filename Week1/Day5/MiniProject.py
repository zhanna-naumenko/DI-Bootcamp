print("Wellcome to TIC TAC TOE!")
#printing the game board

board = [" " for x in range(9)]
def display_board():
    '''Displays the board of the game'''
    frame = ("*" * 17).format(board)
    row1 = "*   {} | {} | {}   *".format(board[0], board[1], board[2])
    row2 = "*  ---|---|---  *".format(board)
    row3 = "*   {} | {} | {}   *".format(board[3], board[4], board[5])
    row4 = "*  ---|---|---  *".format(board)
    row5 = "*   {} | {} | {}   *".format(board[6], board[7], board[8])


    print()
    print("TIC TAC TOE")
    print(frame)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(frame)
    print()


# display_board()

#take player input

def player_input(icon):
    '''Gets the inputs of the player and check where he wants to put his value'''

    print(f"Player {icon}'s turn...")
    choice_row = int(input("Enter row: ").strip())
    choice_column = int(input("Enter column: ").strip())
    choice = 0

    if choice_row == 1:
        choice = choice_column - 1
    elif choice_row == 2:
        choice = choice_column + 2
    elif choice_row == 3:
        choice = choice_column + 5

    if board[choice] == " ":
        board[choice] = icon
    else:
        print("That space is already taken!")

#check for win
def check_win(icon):
    '''Checks the results for winning'''
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for condition in win_conditions:
        if all(board[item] == icon for item in condition):
            return True

    return False


def is_draw():
    '''Checks if there is a draw'''
    return " " not in board

#iterating through the loop while we didn't get one of the results win or draw
while True:
    display_board()
    player_input("X")
    if check_win("X"):
        display_board()
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

    display_board()
    player_input("O")
    if check_win("O"):
        display_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        display_board()
        print("It's a draw!")
        break

