import random

print('\n1. feladat')

def gensquares(N):
    for x in range(N):
        yield x**2

for x in gensquares(10):
    print(x)

print('\n2. feladat')

random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

print('\n3. feladat')

s = 'hello'

for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))

print('\n4. feladat')

my_list = [1,2,3,4,5]

# cash into the gencop generator 
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)