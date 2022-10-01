def add(n1,n2):
    print(n1+n2)

num1 = 20
#num2 = input("Give a number: ")
#add(num1,num2)

try:
    # Want top attempt this code
    # May have an error
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

# OS / Type error
try:
    #f = open('testfile','w')
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("This is a type error")
except OSError:
    print("This is a OS error")
except:
    print("All other exceptions")
finally:
    print("I always run")

def ask_for_int():
    while True:
        try:
            result = int(input("Please give a number: "))
        except:
            print("Whoops! That is not a number!")
            continue
        else:
            print("Yes, thank you")
            break
        # finally:
        #     print("I am going to ask you again \n")

ask_for_int()