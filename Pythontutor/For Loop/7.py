n = int(input())
a = 1
sum = 0

for i in range(1,n+1):
    a*=i
    sum+=a


print(sum)
