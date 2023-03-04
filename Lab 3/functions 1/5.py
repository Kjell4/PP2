#all permutations

def all_permutations(s):
    t = ""
    for i in s:
        t+=i
        for j in range(len(s)):
            if i!=s[j]:
                t+=s[j]
        print(t)
        t=""

string = input()

all_permutations(string)