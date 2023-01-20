list1 = ["a", "b", "c"]             #1
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]             #2
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)



list1 = ["a", "b" , "c"]              #3
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)