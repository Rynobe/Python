from random import shuffle
example = [1,2,3,4,5,6,7]
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

results = shuffle_list(example)
print(results)

mylist = [' ', 'O', ' ']
print(shuffle_list(mylist))

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess= input("Pick a number: 0, 1 or 2: ")
    return int(guess)

print(player_guess())

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong")
        print(mylist)

# Initial List
mylist = [' ', 'O', ' ']
# Shuffle list
mixed_up = shuffle_list(mylist)
# User guess
guess = player_guess()
# Check guess
print(check_guess(mixed_up,guess))