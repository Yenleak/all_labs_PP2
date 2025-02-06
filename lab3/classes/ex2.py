class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length **2

n = int(input())
square = Square(n)
print("area of ​​the square: ", square.area())
shape = Shape()
print("another: ", shape.area())