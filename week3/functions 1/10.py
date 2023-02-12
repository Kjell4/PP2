#remove the duplicates

def list_unique_elements(list):
    cnt = 0
    for i in list:
        for j in list:
            if i==j:
                cnt+=1
                if cnt>1:
                    list.pop(j)
                    cnt-=1
        cnt=0

    print(list)

list1 = []                                   
n = int(input())
for i in range(n):
    list1.append(int(input()))

list_unique_elements(list1)

