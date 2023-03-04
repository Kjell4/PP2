import re

f = open("row.txt","r", encoding="utf8")

f_list = re.sub(r"(?<!\s)(?=[A-Z])", " " ,f.read())

print(f_list)