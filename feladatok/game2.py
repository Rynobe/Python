import numpy as np
x =  np.empty(shape=(11,5),dtype=str)
def format_board():
    idxo=0
    while idxo < 11:
        if idxo % 2 != 0:
            x[idxo][1] = "|"
            x[idxo][3] = "|"
            idxo += 1
        else:
            x[idxo][0] = " "
            x[idxo][2] = " "
            x[idxo][4] = " "
            idxo += 1
    idxs=0
    while idxs < 5:
        x[3][idxs] = "-"
        x[7][idxs] = "-"
        idxs += 1
    print(x)

def display():
    print("Welcome to Tic Tac Toe!")

def XorO():
    player1 = input("Player 1: Do you want to be X or O: ")
    if player1 not in ['X','O']:
        print("Sorry, I don't understand, please choose X or O!")
        XorO()
    else:
        print("Player 1 will go first")
        return player1

def ready_to_start():
    ready = input("Are you ready to play? Enter Yes or No: ")
    if ready not in ["Yes","No"]:
        print("Sorry, I don't understand, please choose Yes or No!")
        ready_to_start()
    if ready == "Yes":
        print(x)
    elif ready == "No":
        print("The game has over.")

def game():
    display()
    XorO()
    ready_to_start()

#game()
format_board()