# 1. Feladat
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# 2. Feladat
def animal_crackers(text):
    x = text.split()
    if x[0][0] == x[1][0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangoroo'))

# 3. Feladat
def old_macdonald(name):
    mylist = list(name)
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    return ''.join(mylist)

print(old_macdonald('macdonalds'))

# 4. Feladat
def master_yoda(text):
    mylist = text.split()
    str_list = []
    x = len(mylist)
    while x > 0:
        str_list.append(mylist[x-1])
        x -= 1
    return ' '.join(str_list)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))