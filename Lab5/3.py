import re

f = open("row.txt", "r", encoding="utf8")

f_list =  re.search(r"([a-z]+_)+[a-z]+", f.read())

print(f_list)
