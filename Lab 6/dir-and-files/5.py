mylist = ['apple', 'banana', 'cherry']

f = open('somefile.txt', 'w')
for element in mylist:
    f.write(element)