import os

path = r'C:\Users\Acer\Desktop\Python'

if os.path.exists(path) == True:
    print("Path exists")
    dirname, filename = os.path.split(path)
    print("Directory portion:", dirname)
    print("Filename portion:", filename)
else:
    print("Path does not exist")