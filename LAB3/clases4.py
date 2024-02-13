import math

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"coordinates({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"new coordinates({self.x}, {self.y})")

    def dist(self, x2, y2):
        print(math.sqrt(((x2 - self.x) ** 2) + ((y2 - self.y) ** 2)))

pnt = Point(50, 45)
pnt.show()
pnt.move(1, 2)
pnt.dist(4, 5)


