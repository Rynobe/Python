
def myfunc(a,b):
    # Returns 5% of the sum of a and b.
    return sum((a,b))*0.05

print(myfunc(40,60))

def myfunc(a,b,c,d=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d))*0.05
print(myfunc(40,60,100))

# Using *args command
def myfunc(*args):
    return sum(args)*0.05
print(myfunc(40,60))

def myfunc(*same):
    return sum(same)*0.05
print(myfunc(40,60))

# Using **kwargs command. It gives a dictionary
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc(fruit='apple', veggie='lettuce')

def myfunc(**valami):
    print(valami)
myfunc(fruit='apple', veggie='lettuce')

# Using **kwargs and *args command
def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[1],kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs', animal='dog')