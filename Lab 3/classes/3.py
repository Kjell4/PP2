class Shape:

    def area(self, s = 0):
        print(self.s)

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.compute_area()

    def compute_area(self):
        self.s = self.length * self.width
        self.area(self.s)


   
rect = Rectangle(int(input()), int(input()))