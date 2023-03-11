upper = 0
lower = 0

for i in str(input()):              #str() - builtin function
    if i>='A' and i<='Z':
        upper+=1
    else:
        lower+=1

print("Number of upper case letters:", upper)
print("Number of lower case letters:", lower)
