from traceback import print_tb


t = (1,2,3)
mylist = [1,2,3]
mydict = {'key1':1,'key2':2,'key3':3,}

print(type(t))
print(type(mylist))
print(type(mydict))

print(len(t))
print(len(mylist))
print(len(mydict))

print()

print(t[0])
print(mylist[1])
print(mydict['key3'])
print()

b = ('a','a','b')
print(b.count('a')) # Hány darab van a keresett értékből.
print(b.index('a')) # Melyik index(eken) van a keresett érték.

print(t)