"""
myfile = open('test.txt')

print(myfile.read())    # A fájl összes tartalmát kiírja egybe.
myfile.seek(0)
print()

print(myfile.readlines()) # Soronként bontja szét.
myfile.seek(0)
print()

myfile.close()  # Mikor végeztem a fájl beolvasásával bezárom.

with open('test.txt') as my_new_file:
    beolvas = my_new_file.read()
print(beolvas)
print()

with open('test.txt', mode='r') as f:  # Read only mode
    print(f.read())
print()

with open('newfile.txt', mode='w') as f:  # write only mode (override or creat new files)
    f.write('I CREATED THIS FILE')
print()
with open('newfile.txt', mode='r') as f:
    print(f.read())
print()

with open('test.txt', mode='a') as f:  # append only mode (add on to files)
    f.write('\nFOUR ON FOURTH')
with open('test.txt', mode='r') as f:
    print(f.read())
print()

with open('test.txt', mode='r+') as f: # reading and writing
    print(f.read())
print()

with open('test.txt', mode='w+') as f: # writing and reading (Overwrites existing file or create a new file!)
    print(f.read())
print()

 """