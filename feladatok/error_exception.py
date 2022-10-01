print("1.Feladat")
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type Error!")

print("\n2.Feladat")
try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Zero Division Error!")
finally:
    print("All Done")

print("\n3.Feladat")
def ask():
    while True:
        try:   
            result = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is: {result**2}")
            break
ask()