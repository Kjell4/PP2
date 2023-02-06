n = int
max = 0
cnt = 0

while n != 0:
    n = int(input())
    if max <= n:
        if max == n:
            cnt+=1
        max = n

print(cnt+1)

