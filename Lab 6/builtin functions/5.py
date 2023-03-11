tuple1 = (1,4,3,4,'s')

x = False

for i in range(0,len(tuple1)):  #len(), range() - builtin functions
    if tuple1[i] == False:
        x = False
        break
    else:
        x = True

if x == True:
    print(True)
else:
    print(False)

        