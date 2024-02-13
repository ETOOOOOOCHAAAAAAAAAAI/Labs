from clases2 import *

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
       return self.length * self.width


rec = Rectangle(400, 500)
print(rec.area())