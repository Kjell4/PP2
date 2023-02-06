n = int
max = 0
cnt = 0

while n != 0:
    n = int(input())
    if max < n:
        max = n
        cnt+=1

print(cnt-1)


    

