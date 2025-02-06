import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getCoordinates(self):
        print(self.x, self.y)

    def moveCoordinates(self, x, y):
        self.x += x
        self.y += y        

    def dist(self, point):
        return math.sqrt((self.x - point.x) **2 + (self.y - point.y) **2)
    
p1 = Point(2, 3)
p2 = Point(3, 4)
p1.getCoordinates()
p2.getCoordinates()
print(p1.dist(p2))
p1.moveCoordinates(2, 2)
p1.getCoordinates()