import math

class Point:

    def __init__(self , x1 , y1):
        self.x1 = x1
        self.y1 = y1
        self.display()

    def display(self):
        print('(' + str(self.x1) +','+ str(self.y1) + ')')
    
    def move(self, x2 , y2):
        self.x2 = x2
        self.y2 = y2
    
    def dist(self):
        print(math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2 )) 
        


p = Point(int(input()), int(input()))
p.move(int(input()), int(input()))
p.dist()
