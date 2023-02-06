n = int
sum = 0
cnt = 0

while n != 0:
    n = int(input())
    sum+=n
    cnt+=1

print(sum/(cnt-1))