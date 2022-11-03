def func():
    return 1

print(func())

def hello():
    return "Hello!"

greet = hello()
print(greet)

# Delete the hello func
del hello
# Error 'cause we delete the hello func
#print(hello())

# It'll run 'cause we save hello func in greet value
print(greet)

def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is the welcome() func inside hello!'
    
    #print(greet())
    #print(welcome())
    print('I am going to return a function!')
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')

# not print(my_new_func) like a value
print(my_new_func())

def cool():
    
    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()
print(some_func())

def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)

def new_decorator(original_func):
    
    def wrap_func():

        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function')
    
    return wrap_func

def func_needs_decorator():
    print('I want to be decorator!!')

decorated_func = new_decorator(func_needs_decorator)
#decorated_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorator!!')

func_needs_decorator()