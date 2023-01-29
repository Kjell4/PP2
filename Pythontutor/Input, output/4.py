n = int(input())

if n < 1440:
    h = n // 60
    m = n % 60
else:
    h = (n-1440) // 60
    m = n % 60

print(h,m)