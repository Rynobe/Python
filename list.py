from secrets import randbelow


mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
print()

mylist = [letter for letter in mystring]
print(mylist)
print()

mylist = [x for x in 'word']
print(mylist)
print()

mylist = [num for num in range(0,11)]
mylist2 = [num**2 for num in range(0,11)]
print(mylist)
print(mylist2)
print()

mylist = [x for x in range(0,11) if x%2==0]
mylist2 = [x**2 for x in range(0,11) if x%2==0]
print(mylist)
print(mylist2)
print()

celcius = [0,10,20,34.5]
farenheit = [((9/5)*temp + 32) for temp in celcius]
print(farenheit)
print()

farenheit = []
for temp in celcius:
    farenheit.append((9/5)*temp + 32)
print(farenheit)
print()

# For and if statement 
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)
print()

# nested loop
mylist = []
for x in [2,4,6]:
    for y in [1,10,100]:
        mylist.append(x*y)
print(mylist)
print()

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)
print()