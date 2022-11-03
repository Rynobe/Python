from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]

a = Counter(mylist)
print(a)

mylist = ['a','a',10,10,10]
b = Counter(mylist)
print(b)

print(Counter('aaaaaabbbbdddssss'))