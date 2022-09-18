def square(num):
    return num**2

my_nums=[1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

############################
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names)))

# filter retrun True or False value
############################
my_nums=[1,2,3,4,6]

def check_even(num):
    return num%2 == 0

print(list(filter(check_even,my_nums)))

for n in filter(check_even,my_nums):
    print(n)

# Lambda 
############################
def square(num):
    result = num ** 2
    return result

print(square(3))

square = lambda num:num**2
print(square(5))

print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num:num%2 == 0,my_nums)))

print(list(map(lambda x:x[::-1],names)))

# Nested statements & scope
#################################
print('\nNested statements & scope:')

x = 25
def printer():
    x = 50
    return x

print(x)
print(printer())

# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():

    # ENCLOSING
    name = 'Sammy'

    def hello():

        # LOCAL
        name = 'I AM LOCAL'
        
        print(f'HELLO {name}')
    hello()
greet()

x = 50
def func():
    global x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
func()
print()

# OR

x = 50
def func(x):
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x
x = func(x)
print(x)