
print("Welcome to Tic Tac Toe!")

first_row = [[" "],[" "],[" "]]
second_row = [[" "],[" "],[" "]]
third_row = [[" "],[" "],[" "]]
playing_board = [first_row,second_row,third_row]

def display_board():
    """Displaying the board"""
    tictactoe_board = f"""TIC TAC TOE
    *********************
    *    {first_row[0][0]}  |  {first_row[1][0]}  |  {first_row[2][0]}    *
    *   ----|-----|----   *
    *    {second_row[0][0]}  |  {second_row[1][0]}  |  {second_row[2][0]}    *
    *   ----|-----|----   *
    *    {third_row[0][0]}  |  {third_row[1][0]}  |  {third_row[2][0]}    *
    *********************"""
    print(tictactoe_board)
# display_board()

def player_input(player):
    """Puts player input into the board"""
    user_row = int(input("Enter row number: "))
    user_column = int(input("Enter column number: "))
    playing_board[user_row - 1][user_column - 1][0] = player


def check_win(board, player):
    """Checks if player won the game"""
    if ((board[0][0][0]==player and board[0][1][0]== player and board[0][2][0]==player )or #for row1

            (board[1][0][0]==player and board[1][1][0]==player and board[1][2][0]==player )or #for row2

            (board[2][0][0]==player and board[2][1][0]==player and board[2][2][0]==player )or #for row3

            (board[0][0][0]==player and board[1][0][0]==player and board[2][0][0]== player )or#for Colm1

            (board[0][1][0]==player and board[1][1][0]==player and board[2][1][0]==player )or #for Colm 2

            (board[0][2][0]==player and board[1][2][0]==player and board[2][2][0]==player )or #for colm 3

            (board[0][0][0]==player and board[1][1][0]==player and board[2][2][0]==player )or #daignole 1

            (board[0][2][0]==player and board[1][1][0]==player and board[2][0][0]==player )):#daignole 2
        return True
    return False


def check_tie(board):
    """Checks if the game has resulted in a tie"""
    # Check if there is any empty space left
    for row in board:
        for cell in row:
            if cell[0] == " ":
                return False
    return True


def play_game(board):
    """Play the game"""
    players = ["X", "O"]
    display_board()
    while True:
        for player in players:
            print(f"Player's {player} turn...")
            player_input(player)
            display_board()

            if check_win(board, player):
                print(f"Player {player} wins!")
                return
            if check_tie(board):
                return

play_game(playing_board)






