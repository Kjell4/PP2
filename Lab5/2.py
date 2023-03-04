import re

f = open("row.txt", "r", encoding="utf8")

f_list = re.findall(r".*a+.*b+.*b+.*b*.*", f.read())

for element in f_list:
    print(element)