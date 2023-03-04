#filter prime numbers

def filter_primes(list):
    list2 = []
    cnt=0
    for i in list:
        for j in range(1, int(i)+1):
            if(int(i)%j==0):
                cnt+=1
        if cnt==2:
            list2.append(i)
        cnt = 0
    print(list2)

list1 = []                           
n = int(input())

for i in range(n):
    list1.append(int(input()))

filter_primes(list1)