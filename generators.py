def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)
# OR
print(list(create_cubes(10)))

print('\nFibonac')
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
# OR
print(list(gen_fibon(10)))

print('\nSimple')
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

# StopIteration error 'cause not next value.
#print(next(g))

print('\nString')
s = "Hello"

for letter in s:
    print(letter)

# Error 'cause 'str' object is not an iterator
#next(s)
s_iter = iter(s)
print(next(s_iter))