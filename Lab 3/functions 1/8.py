# spy game

def spy_game(list):
    x = False
    for i in range(len(list)-2):
        if list[i]==0 and list[i+1]==0 and list[i+2]:
            x = True
    if x==True:
        print(True)
    else:
        print(False)

n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))

spy_game(list1)
