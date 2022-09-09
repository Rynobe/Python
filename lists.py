my_list = [1,2,3]
my_list2 = ['szöveg',100,23.2]

print(len(my_list))
print(len(my_list2))
print(my_list2[0])
print(my_list[1:])

print(my_list + my_list2)   # Listák összeadása.

print(my_list)
my_list[0] = 'Hello'    # Ezzel felülírjuk az első elemét a listának.
print(my_list)

my_list.append('six')   # Az utolsó elem után beszurunk egy új elemet.
print(my_list)

my_list.pop()   # Töröljük az utolsó elemét a listának. 
print(my_list)

popped_list = my_list.pop() # A törölni kívánt elemet elmentjuk egy másik listába.
print(popped_list)

my_list2.pop(0) # Az első elemet a listából töröljük.
print(my_list2)

string_list = ['d','a','c','b']
num_list = [4,9,1,6]

string_list.sort()   # Sorrendbe rakja a listát.
num_list.sort()
print(string_list)
print(num_list)