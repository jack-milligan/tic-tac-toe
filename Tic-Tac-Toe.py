#Function to create an the game board:

from IPython.display import clear_output
#print('\n'*100)

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
#Function that picks which player goes first:

import random
def choose_first():
    if random.randint(0,1) == 0 : 
        return('Player 1 will be going first')
    else:
        return('Player 2 will be going first')

#Function that assigned X or O to the players:
def player_input():
    marker = ''
    while marker != 'X' and marker !='O':
        marker = input('Player 1 choose X or O: ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2='X'
    return(player1,player2)
    
#Function that places the X or O on the board
def place_marker(board, marker, position):
    board[position] = marker

#Function to check if there has been a winner
    
def win_check(board, mark):
    #ALL COLUMNS, ALL ROWS, AND ALL DIAGONALS NEED TO BE CHECKED
    return((board[1] == mark and board[2]==mark and board[3]==mark)   #ROW
           or(board[4] == mark and board[5]==mark and board[6]==mark) #ROW
           or(board[7] == mark and board[8]==mark and board[9]==mark) #ROW
           or(board[1] == mark and board[4]==mark and board[7]==mark) #COLUMN
           or(board[2] == mark and board[5]==mark and board[8]==mark) #COLUMN
           or(board[3] == mark and board[6]==mark and board[9]==mark) #COLUMN
           or(board[1] == mark and board[5]==mark and board[9]==mark) #DIAGONAL
           or(board[3] == mark and board[5]==mark and board[7]==mark))#DIAGONAL
           
#Function that checks if there is available space on the board:

def space_check(board, position):
    return board[position] == ' '  

#Function that checks if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            #IF SPACE_CHECK IS TRUE (THERE IS A SPACE WITHIN THE BOARD) 
            #THE BOARD IS NOT FULL SO WE RETURN FALSE
            return False
    #BOARD IS FULL    
    return True

#Function that allows the player to pick their location on the board:

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))
    return position
    
#Function that asks if both players would like to play again:

def replay():
    r = input('Would you like to play again? (Yes or No): ')
    if r.lower() == 'yes':
        return True
    else:
        return False
        
#This is all of the functions put together to create the game itself:

print('Welcome to Tic Tac Toe!')

while True:
    #RESET THE BOARD
    from IPython.display import clear_output
    import random
    board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    game = input('Do you want to play Tic Tac toe?: ')
    if game.lower()== 'yes':
        game_on = True
    else:
        game_on= False
    
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1 will be going first':
            #SHOWS THE PLAYER THE BOARD
            display_board(board)
            #PICKS A LOCATION ON THE BOARD
            position = player_choice(board)
            #PLACES THE MARKER ON THE BOARD LOCATION
            place_marker(board, player1_marker, position)
            
            #DID PLAYER 1 WIN?
            if win_check(board,player1_marker):
                display_board(board)
                print('Congratulations, you have won the game!')
                game_on = False
            #DID PLAYER 1 AND 2 TIE?
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
            #IT IS NOW PLAYER 2'S TURN
                else:
                    turn='Player 2 will be going first'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            #DID PLAYER 2 WIN?
            if win_check(board,player2_marker):
                display_board(board)
                print('Congratulations, you have won the game!')
                game_on = False
            #DID PLAYER 2 AND PLAYER 1 TIE?
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
            #IT IS NOW PLAYER 1'S TURN
                else:
                    turn='Player 1 will be going first'
                    
    #DO BOTH PLAYERS WANT TO PLAY AGAIN?
    if not replay():
        break
