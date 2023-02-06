last = int(input())
cnt = 0
next = int
while next != 0:
    next = int(input())
    if last < next:
        cnt+=1
    last = next

print(cnt)


    
