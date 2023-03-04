# 3 next to 3

def has_33(list):
    x = False
    a = 0
    b = 0
    for i in range(len(list)):
        if i%2==0:
            a = list[i] 
            if a==b==3:
                x = True
        else:
            b = list[i]
            if a==b==3:
                x = True
    if x==True:
        print(True)
    else:
        print(False)

n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))

has_33(list1)


