def squares(n):
    i = 1
    while i*i<=n:
        yield i*i
        i += 1

x = int(input())

for i in squares(x):
    print(i)
