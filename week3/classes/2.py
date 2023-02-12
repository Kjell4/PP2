class Shape:

    def area(self, s = 0):
        print(self.s)

class Square(Shape):

    def __init__(self, length):
        self.length = length
        self.s = int(length)**2
        self.area(self.s)
        

sqr = Square(input())