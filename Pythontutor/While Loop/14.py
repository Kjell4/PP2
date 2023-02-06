n = int(input())

n1 = 0
n2 = 1
cnt = 2
n3 = 1
x = False

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while n3 <= n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        cnt+=1
        if n == n3:
            x = True
    if x == False:
        print(-1) 
    else:     
        print(cnt-2)

