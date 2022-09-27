def display(game_list):
    print(f"Here is the current list:\n{game_list}")

def give_position():
    acceptable_range = range(3)
    within_range = False

    while within_range==False:
        position = input("Pick a position to replace (0,1,2): ")
        if position.isdigit() == False:
            print("Sorry that is not a digit!")
        else:
            if int(position) in acceptable_range:
                within_range = True
            else:
                print("Not in range")
                pass
    return int(position)

def continues():
    allitas = input("Would you like to keep playing? Y or N: ")
    if allitas == 'Y':
        display(game_list)
        replace(game_list,give_position())
    elif allitas == 'N':
        print(f"Here is the last list:\n {game_list}")
    else:
        pass

def replace(game_list, position):
    new_string = input("Type a string to place at the position: ")
    game_list[position] = new_string
    display(game_list)
    continues()

game_list = [1,2,3]
display(game_list)
replace(game_list,give_position())