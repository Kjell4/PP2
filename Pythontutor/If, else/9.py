x1 = int(input())                                       #1 slon , 2 figura
y1 = int(input()) 
x2 = int(input())              
y2 = int(input())              

if abs(x1-x2)==abs(y1-y2) and x1!=x2 and y1!=y2:
    print("YES")
else:
    print("NO")