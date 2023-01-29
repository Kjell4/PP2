x1 = int(input())                                       #1 ladia , 2 figura
y1 = int(input()) 
x2 = int(input())              
y2 = int(input())              

if x1==x2:
    if y1 != y2:
        print("YES")
elif y1==y2:
    if x1 != x2:
        print("YES")
else:
    print("NO")