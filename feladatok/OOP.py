import math
# 1. Feladat
print("\n1.Feladat")
class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt(((x2-x1)**2 + (y2-y1)**2))

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

# 2. Feladat
print("\n2.Feladat")
class Cylinder():
    
    def __init__(self,height=1,radius=1):
        self.pi = 3.14
        self.height = height
        self.radius = radius
        
    def volume(self):
        result = self.pi*(self.radius*self.radius)*self.height
        return result
    
    def surface_area(self):
        result = 2*self.pi*(self.radius*self.radius) + 2*self.pi*self.radius*self.height
        return result

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())