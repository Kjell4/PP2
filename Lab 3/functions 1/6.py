#reversed words

def reverse(s):
    list = []
    t=""
    for i in range(0,len(s)):
        if i==len(s)-1:
            t+=s[i]
            list.append(t)
        elif s[i]!=" ":
            t+=s[i]
        elif s[i]==" ":
            list.append(t)
            t=""
    for i in range(len(list)-1,-1,-1):
        print(list[i], end=" ")


string = input()

reverse(string)