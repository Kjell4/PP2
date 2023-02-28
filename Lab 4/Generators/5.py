def myreverse(n):
    while n!=-1:
        yield n
        n-=1

x = int(input())

for i in myreverse(x):
    print(i)