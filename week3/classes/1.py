class String:

    def getString(self, string):
        self.string = string.upper()
        
    def printString(self):
        print(self.string) 

s = String()
s.getString(input())
s.printString()