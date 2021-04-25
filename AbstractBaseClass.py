# introduction abstract class

from abc import ABC ,abstractmethod

class Shape:
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    
    def printarea(self):
        return self.length * self.breath

r=Rectangle(3,4)
area=r.printarea()
print("Area of Rectangle is :  ",area)
 