#check to palindrome

def ispalindrome(s):                                     
    t = ""

    for i in range(len(s)-1,-1,-1):
        t+=s[i]

    if s == t:
        print("palindrome")
    else:
        print("not palindrome")

string = input()

ispalindrome(string)


