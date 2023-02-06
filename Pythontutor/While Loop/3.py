n = int(input())

i = 2
cnt = 2
a = i*i

if n == 1:
    print(0,1)
elif n == 2:
    print(1,2)
elif n == 3:
    print(1,2)
else:
    while a*i <= n:
        a*=i
        cnt+=1
        
    print(cnt , a)