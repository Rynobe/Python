# 1. Feladat
print("1. Feladat")
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
print("\n2. Feladat")
def animal_crackers(text):
    x = text.split()
    if x[0][0] == x[1][0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangoroo'))

# 3. Feladat
print("\n3. Feladat")
def old_macdonald(name):
    mylist = list(name)
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    return ''.join(mylist)

print(old_macdonald('macdonalds'))

# 4. Feladat
print("\n4. Feladat")
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

# 5. Feladat
print("\n5. Feladat")
def almost_there(n):
    mylist = [100,200]
    if n >= 90 and n <= 110:
        return True
    elif n >= 190 and n <= 210:
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(204))

# 6. Feladat
print("\n6. Feladat")
def laughter(pattern, text):
    return text.count(pattern)

print(laughter('hah','hahahah'))

# 7. Feladat
print("\n7. Feladat")
def paper_doll(text):
    mylist = []
    for letter in text:
        db = 3
        while db > 0:
            mylist.append(letter)
            db -= 1
    return ''.join(mylist)

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# 8. Feladat
print("\n8. Feladat")
def spy_game(nums):
    mylist = []
    for i in nums:
        if i==0 or i==7:
            mylist.append(i)
    if mylist[0]==0 and mylist[1]==0 and mylist[2]==7:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# 9. Feladat
print("\n9. Feladat")
def makes_twenty(n1,n2):
    szam = n1+n2
    if szam == 20:
        return True
    elif n1==20 or n2==20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# 10. Feladat
print("\n10. Feladat")
def has_33(nums):
    mylist = []
    for idx,num in enumerate(nums):
        print(nums[idx])
        print(nums[idx])


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))