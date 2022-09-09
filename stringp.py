name = "Patrik"
print(name[0])

last_letter = name[-1:]
print(last_letter)
print(name[0:5] + 'cia')

x = "Hello World"
print(x)
x = x + " it is beautiful outside!"
print(x)

letter = "z"
print(letter * 10)  # 10x kiírja a z betűt.

lag = "Hello Patrik"
print(lag.upper())
print(lag.lower())
print(lag.split())      # a szavakat feldarabolja.
print(lag.split()[1])   # A második szót íjra ki.

print('This is a simple exercise {}'.format('Format'))
print('The {0} {1} {2}'.format('orange','fast','fox'))
print('The {s} {b} {c}'.format(b='black',s='small',c='cat'))


result = 100/777
print(result)
print('result: {r:1.2f}'.format(r=result))
print('result: {r:10.5f}'.format(r=result)) # mennyi tizedestörtet mutasson.

name = "Jose"
print(f'Hello, his name is {name}') # Ez a Python 3.6-os verzióban jött ki.

age = 22
print(f'{name} is {age} years old')


