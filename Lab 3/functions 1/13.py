import random

x = random.randint(1,20)
num = 0

print("Hello! What is your name?")
name = input()

txt1 = "Well, {}, I am thinking of a number between 1 and 20. \nTake a guess."
txt2 = "Good job, {}! You guessed my number in {} guesses!"


print(txt1.format(name))
n = int(input())

while x!=n:
    if x > n:
        print("Your guess is too low. \nTake a guess.")
        num+=1
        n = int(input())
    elif x < n:
        print("Your guess is too big. \nTake a guess.")
        num+=1
        n = int(input())
else:
    num+=1
    print(txt2.format(name,num))