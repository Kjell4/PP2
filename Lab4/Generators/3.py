def dev34(n):
    i = 0
    while i<=n:
        if i%3==0 and i%4==0:
            yield i
        i+=1

x = int(input())

for i in dev34(x):
    print(i)