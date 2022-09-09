# A kulcsok mindig string típusúak!!

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

o_dict = {'apple': 2.99,'samsung':1.99,'nokia':5.80}
print(o_dict)
print(o_dict['apple'])

d = {'k1':123,'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['insideKey'])

d['k4'] = 300   # Új elem hozzáadása.
print(d)

d['k1'] = 'Felülirva'  # Meglévő elem felülírása.
print(d)

print(d.keys())
print(d.values())
print(d.items())
