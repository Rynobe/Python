from cgi import print_arguments
from re import I, M


mylist = [1,2,3,4,5,6,7,8,9,10]
"""
for num in mylist:
    print(num)

for num in mylist:
    print('Hello')

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f'Even number: {num}')
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

print(list_sum)

mystring = "Hello World"
for letter in mystring:
    print(letter)


tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
print()

for item in mylist:
    print(item)
print()

for (a,b) in mylist:
    print(a)
    print(b)
print()

for a,b in mylist:
    print(b)
print()

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
    print(b)
print()

mystring = 'Sanny'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

mystring = 'Sanny'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

"""
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
print()

for key,value in d.items():
    print(value)
print()