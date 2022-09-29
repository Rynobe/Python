import random
import os

def display_board(board):
    os.system('cls')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    marker = ''

    # KEEP ASKING PLAYER 1 to choose X or O

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()

    # ASSIGN PLAYER 2, the opposite marker
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    flip=0
    if flip%2 == 0:
        flip += 1
        return 'Player 1'
    else:
        flip += 1
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_borad_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
    return position

def replay():
    choise = input("Play again? Enter Yes or No: ")
    return choise == 'Yes'

print('Welcome to Tic Tac Toe!')
while True:
    turn = choose_first()
    board = [' ']*10
    player1_marker , player2_marker = player_input()
    print(f"{turn} will go first.")
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print('Player 1 Has Won!')
                game_on = False
            else:
                if full_borad_check(board):
                    display_board(board)
                    print('TIE Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print('Player 2 Has Won!')
                game_on = False
            else:
                if full_borad_check(board):
                    display_board(board)
                    print('TIE Game!')
                    game_on = False
                else:
                    trun = 'Player 1'

    if not replay():
        break