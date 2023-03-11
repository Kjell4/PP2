f = open('somefile.txt', 'r')
count = 0
for line in f:
    count += 1

print("Number of lines:", count)