n = int
max1 = max2 = 0

while n != 0:
    n = int(input())
    if max1 < n:
        max2 = max1
        max1 = n

print(max2)
