from contextlib import nullcontext
import numpy as np

x =  np.empty(shape=(5,5),dtype=str)

def position(value,db):
    if db % 2 != 0:
        print("Player 2 will come")
        db += 1
    elif db != 0:
        print("Player 1 will come")
        db += 1
    else:
        pass

    within_range = False
    while within_range==False:
        pos = input("Choose your next position (1-9): ")
        if pos.isdigit() == False:
            print("Sorry that is not a digit!")
        else:
            if int(pos) in range(1,10):
                within_range = True
            else:
                print("Not in range")
                position(value,db)
    if int(pos) == 1:
        x[0][0] = value
    elif int(pos) == 2:
        x[0][2] = value
    elif int(pos) == 3:
        x[0][4] = value
    elif int(pos) == 4:
        x[2][0] = value
    elif int(pos) == 5:
        x[2][2] = value
    elif int(pos) == 6:
        x[2][4] = value
    elif int(pos) == 7:
        x[4][0] = value
    elif int(pos) == 8:
        x[4][2] = value
    elif int(pos) == 9:
        x[4][4] = value
    print(x)
    position(value,db)

def format_board():
    idxo=0
    while idxo < 5:
        x[idxo][1] = "|"
        x[idxo][3] = "|"
        x[idxo][0] = " "
        x[idxo][2] = " "
        x[idxo][4] = " "
        idxo += 1
    idxs=0
    while idxs < 5:
        x[1][idxs] = "-"
        x[3][idxs] = "-"
        idxs += 1

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
        return ready
    elif ready == "No":
        print("The game has over.")
        return ready

def game():
    db = 0
    format_board()
    display()
    result = XorO()
    ready = ready_to_start()
    if ready == "Yes":
        position(result,db)
    else:
        pass

game()
