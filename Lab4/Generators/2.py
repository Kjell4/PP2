def evennum(n):
    i = 0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

x = int(input())

for i in evennum(x):
    print(i)