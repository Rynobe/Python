"""
# Count list elem value
mylist = [1,2,3,4]
print(mylist.pop())
print()
print(help(mylist.insert))
"""

# def Function
import re


def say_hello():
    print("Hello")
say_hello()

def say_hello(name):
    print(f'Hello {name}')
say_hello('Patrik')

def say_hello(name='Default'):
    print(f'Hello {name}')
say_hello()

def add_num(num1,num2):
    return num1+num2
result = add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(1,20)
result = return_result(1,20)
print(result)

def myfunc(a,b):
    print(a+b)
    return a+b

# Same
result = myfunc(1100,20)
print(result)
print()

def sum_num(num1,num2):
    return num1+num2

print(sum_num(15,30))
print(sum_num('15','30'))

