
import os

# Path to list directories and files
path = r'C:\Users\Acer\Desktop\Python'

print("Directories and Files:")
for entry in os.listdir(path):
    print(entry)