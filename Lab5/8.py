import re

f = open("row.txt","r", encoding="utf8")

f_list = re.split(r"[A-Z]", f.read())

print(f_list)