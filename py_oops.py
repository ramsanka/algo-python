#OOPS
#1. classes
#2. base class
#3. methods/function.
#4. abstract
#5. inheritance.
#6. polymorphism

import math

class Line:

    def __init__(self, c1, c2):
        self.x1 = c1[0]
        self.y1 = c1[1]

        self.x2 = c2[0]
        self.y2 = c2[1]
        
        print(f"the x1-{self.x1} y1-{self.y1}")
        print(f"the x2-{self.x2} y2-{self.y2}")

    def distance(self):
        diffx = self.x2-self.x1
        diffy = self.y2-self.y1
        result = (diffy**2) - (diffx**2)
        self.distance = math.sqrt(result)
        #result = (((self.x2-self.x1)**2) - ((self.y2-self.y1)**2))
        #self.distance = math.sqrt(result)
        #self.distance = 0
        print(self.distance)

    def slope(self):
        self.slope = (self.y2-self.y1)/(self.x2-self.x1)
        print(self.slope)

    #should return a string type and not a non-type
    #dendar methods... overriding the standard methods
    #with your defintion.
    def __str__(self):
       return f"x1 {self.x1} x2 {self.x2}"
       

c1 = (3,2)
c2 = (4,5)

l1 = Line(c1,c2)

l1.distance()
l1.slope()

print(l1)
print(list)