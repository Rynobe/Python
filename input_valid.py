
r = 2

# input tpye default is string
result = input("Please enter a value: ")
print(result)
print(type(result))

# Convert to int
result = input("Please enter a value: ")
int_result = int(result)
print(int_result)
print(type(int_result))

some_number = '100'
print(some_number.isdigit())

# User input valid
def user_check():
    choise = 'WRONG'
    while choise.isdigit() == False:
        choise = input("Please enter a number (1-10): ")
        if choise.isdigit() == False:
            print("Sorry that is not a digit!")
    return int(choise)

print(user_check())

# 
def user_check2():
    # VARIABLES 

    # Initial
    choise = 'WRONG'
    acceptable_range = range(1,10)
    within_range = False
    
    # TWO CONDITIONS TO CHECK
    # DIGIT OR WHITIN_RANGE==False
    while choise.isdigit() == False or within_range==False:
        
        choise = input("Please enter a number (1-10): ")

        # DIGIT CHECK
        if choise.isdigit() == False:
            print("Sorry that is not a digit!")
        else:
            if int(choise) in acceptable_range:
                within_range = True
            else:
                print("Not in range")
                pass
user_check2()