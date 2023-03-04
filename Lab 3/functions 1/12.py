#histogram

def histogram(list):
    for i in range(len(list)):
        for j in range(int(list[i])):
            print("*", end="")
        print()


list1 = []                                   
n = int(input())
for i in range(n):
    list1.append(int(input()))

histogram(list1)
