
playing_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def display_board(board):
    """Displaying the board"""
    board = f"""TIC TAC TOE
*******************
*    {board[0][0]} | {board[0][1]} | {board[0][2]}     *
*   ___|___|___    *
*    {board[1][0]} | {board[1][1]} | {board[1][2]}     *
*   ___|___|___    *
*    {board[2][0]} | {board[2][1]} | {board[2][2]}     *
*      |   |       *  
*******************"""
    print(board)

def player_input(player):
    """Puts player input into the board"""
    user_row = int(input("Enter your row: "))
    user_column = int(input("Enter your column: "))
    playing_board[user_row - 1][user_column - 1] = player
    return playing_board

def check_winner(board, player):
    """Checks if player won the game"""
    if ((board[0][0] == player and board[0][1] == player and board[0][2]== player) or #Row1
    (board[1][0] == player and board[1][1] == player and board[1][2]== player) or #Row2
    (board[2][0] == player and board[2][1] == player and board[2][2]== player) or #Row3
    (board[0][0] == player and board[1][0] == player and board[2][0]== player) or #Column1
    (board[0][1] == player and board[1][1] == player and board[2][1]== player) or #Column2
    (board[0][2] == player and board[1][2] == player and board[2][2]== player) or #Column3
    (board[0][0] == player and board[1][1] == player and board[2][2]== player) or #Diagonal1
    (board[0][2] == player and board[1][1] == player and board[2][0]== player)):#Diagonal2
        return True
    return False

def check_tie(board):
    """Checks if the game has resulted in a tie"""
    for row in board:
        if " " in row:
            return False
    return True

def play_game(board):
    """Play the game"""
    players = ["X", "O"]
    display_board(board)
    while True:
        for player in players:
            print(f"Player {player} tern...")
            player_input(player)
            display_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                return
            if check_tie(board):
                print("It is a tie!")
                return

play_game(playing_board)






