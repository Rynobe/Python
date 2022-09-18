from cmath import pi
from hashlib import new
from itertools import count
from traceback import print_tb

print('\n1. feladat')
def vol(rad):
    return (4/3)*(pi)*(rad**3)
print(vol(2))

print('\n2. feladat')
def ran_check(num,low,high):
    if num in range (low,high+1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f"{num} isn't in the range between {low} and {high}"

print(ran_check(1,2,7))
print(ran_check(5,2,7))

print('\n3. feladat')
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    low = up = 0
    for item in s:
        if item.isupper():
            up += 1
        elif item.islower():
            low += 1
        else:
            pass
    return f'Number of Upper case characters: {up}\nNumber of Lower case characters: {low}'

print(up_low(s))

print('\n4. feladat')
def unique_list(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(unique_list([1,1,1,2,2,2,3,3,3,4,4,5]))

print('\n5. feladat')
def multiply(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result

print(multiply([1,2,3,-4]))
