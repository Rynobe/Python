class Dog():
    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self,mybreed,name,sports):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.my_attribute = mybreed
        self.name = name
        
        # Except boolean True/False
        self.spots = sports
    
    # Operations/Actions --> Methods
    def bark(self,number):
        print("Woof! My name is {} and the number {}".format(self.name,number))


my_dog = Dog(mybreed='Huskie',name='Sammy',sports=False)
print(type(my_dog))
print(my_dog.my_attribute)
print(my_dog.name)
#print(my_dog.spots)
print(my_dog.species)

# bark method use 
my_dog.bark(10)
print()

class Circle():
    # Class object attribute
    pi = 3.14
    
    # def __init__(self,radius):
    #     self.rad = radius

    def __init__(self,radius=1):
        self.rad = radius
        self.area = radius*radius*Circle.pi

    # Method
    # def get_circumfrence(self):
    #     return self.rad * self.pi * 2

    def get_circumfrence(self):
        return self.rad * Circle.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.get_circumfrence())
print(my_circle.area)
print()

