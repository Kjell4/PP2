thistuple = ("apple", "banana", "cherry")       #1
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")       #2
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry")       #3
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1