class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input())
width = int(input())
area_of_react = Rectangle(length, width)
print(area_of_react.area())
