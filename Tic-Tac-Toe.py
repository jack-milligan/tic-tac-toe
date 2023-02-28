"""
Author: Jack, https://github.com/jack-milligan
This is an implementation of the game Tic Tac Toe. Two players take turns placing their
symbol (either "X" or "O") on a 3x3 grid, trying to get three of their symbols in a row (horizontally,
vertically, or diagonally) before the other player does.

To start the game, run the `play_game()` function. This function will prompt each player to enter their
name and symbol, and then alternate turns until the game is won or tied. At the end of the game, the
function will print the final board state and the winner (or "Tie" if there is no winner).

"""


def display_board(board):
    """
    This function displays the game board.

    Args:
    board (list): A list of strings representing the current state of the game board.

    Returns:
    None
    """
    clear_output()

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


def choose_first():
    """
    This function randomly selects which player goes first.

    Args:
    None

    Returns:
    str: A string indicating which player will go first.
    """
    if random.randint(0, 1) == 0:
        return ('Player 1 will be going first')
    else:
        return 'Player 2 will be going first'


def player_input():
    """
    This function allows the players to choose which marker they would like to use.

    Args:
    None

    Returns:
    tuple: A tuple containing two strings, one for each player's marker.
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O: ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


def place_marker(board, marker, position):
    """
    This function places a player's marker on the game board.

    Args:
    board (list): A list of strings representing the current state of the game board.
    marker (str): A string representing the marker to be placed on the board.
    position (int): An integer representing the position on the board where the marker should be placed.

    Returns:
    None
    """
    board[position] = marker


def win_check(board, mark):
    """
    This function checks if a player has won the game.

    Args:
    board (list): A list of strings representing the current state of the game board.
    mark (str): A string representing the player's marker.

    Returns:
    bool: True if the player has won, False otherwise.
    """
    return ((board[1] == mark and board[2] == mark and board[3] == mark)  # ROW
            or (board[4] == mark and board[5] == mark and board[6] == mark)  # ROW
            or (board[7] == mark and board[8] == mark and board[9] == mark)  # ROW
            or (board[1] == mark and board[4] == mark and board[7] == mark)  # COLUMN
            or (board[2] == mark and board[5] == mark and board[8] == mark)  # COLUMN
            or (board[3] == mark and board[6] == mark and board[9] == mark)  # COLUMN
            or (board[1] == mark and board[5] == mark and board[9] == mark)  # DIAGONAL
            or (board[3] == mark and board[5] == mark and board[7] == mark))  # DIAGONAL


def space_check(board, position):
    """
    This function checks if a position on the board is available.

    Args:
    board (list): A list of strings representing the current state of the game board.
    position (int): An integer representing the position on the board to be checked.

    Returns:
    bool: True if the position is available, False otherwise.
    """
    return board[position] == ' '


def full_board_check(board):
    """
    This function checks if the game board is full.

    Args:
    board (list): A list of strings representing the current state of the game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for i in range(1, 10):
        if space_check(board, i):
            # IF SPACE_CHECK IS TRUE (THERE IS A SPACE WITHIN THE BOARD)
            # THE BOARD IS NOT FULL SO WE RETURN FALSE
            return False
    # BOARD IS FULL
    return True


def player_choice(board):
    """
    This function allows a player to choose a position on the game board.

    Args:
    board (list): A list of strings representing the current state of the game board.

    Returns:
    int: An integer representing the position on the board chosen by the player.
    """
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))
    return position


def replay():
    """
    This function asks the players if they want to play again.

    Args:
    None

    Returns:
    bool: True if the players want to play again, False otherwise.
    """
    r = input('Would you like to play again? (Yes or No): ')
    if r.lower() == 'yes':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # RESET THE BOARD
    from IPython.display import clear_output
    import random

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    game = input('Do you want to play Tic Tac toe?: ')
    if game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1 will be going first':
            # SHOWS THE PLAYER THE BOARD
            display_board(board)
            # PICKS A LOCATION ON THE BOARD
            position = player_choice(board)
            # PLACES THE MARKER ON THE BOARD LOCATION
            place_marker(board, player1_marker, position)

            # DID PLAYER 1 WIN?
            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations, you have won the game!')
                game_on = False
            # DID PLAYER 1 AND 2 TIE?
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                # IT IS NOW PLAYER 2'S TURN
                else:
                    turn = 'Player 2 will be going first'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            # DID PLAYER 2 WIN?
            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations, you have won the game!')
                game_on = False
            # DID PLAYER 2 AND PLAYER 1 TIE?
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                # IT IS NOW PLAYER 1'S TURN
                else:
                    turn = 'Player 1 will be going first'

    # DO BOTH PLAYERS WANT TO PLAY AGAIN?
    if not replay():
        break
