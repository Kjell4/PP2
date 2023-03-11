s = input()
r = ""

for i in range(len(s)-1,-1,-1):         #range(), len() - builtin functions
    r+=s[i]

if s == r:
    print("Palindrome")
else:
    print("Not Palindrome")