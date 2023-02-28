def squares(a,b):
    i = a
    while i*i>=a and i*i<=b:
        yield i*i
        i+=1

a = int(input())
b = int(input())

for i in squares(a,b):
    print(i)

