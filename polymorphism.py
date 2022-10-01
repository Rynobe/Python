class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()
print()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof!")

    def eat(self):
        print("I am a dog and I eating")

    def who_am_i(self):
        print("I am a dog!")

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()
print()

# Polimorph 1.0

class Cat():
    def __init__(self,name):
        self.name = name
    
    def shout(self):
        return self.name + " says meow!"

class Fish():
    def __init__(self,name):
        self.name = name
    
    def shout(self):
        return self.name + " says blutty!"

cica = Cat("Manfi")
hal = Fish("Frenky")

for pet in [cica,hal]:
    print(type(pet))
    print(pet.shout())
print()
# Or
def pet_speak(pet):
    print(pet.shout())
pet_speak(cica)
pet_speak(hal)

# Polimorph 2.0

class Pets():
    def __init__(self):
        print("Animal Created")

    def speaks(self,speak):
        print(f"My speak voice is: {speak}")

class Cat(Pets):
    def __init__(self):
        super().__init__()
    
    def speaks(self, speak):
        return super().speaks(speak)

class Fish(Pets):
    def __init__(self):
        super().__init__()
    
    def speaks(self, speak):
        return super().speaks(speak)

cica = Cat()
cica.speaks("Miao")
hal = Fish()
hal.speaks("Gluty")
print()

# Polimorph 3.0
print("Polimorph 3.0")
class Pets():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subcalss must implement this abstract method")

class Dog(Pets):
    def speak(self):
        return self.name + " says woof!"
        
class Cat(Pets):
    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())
