import re

f = open("row.txt","r", encoding="utf8")

f_list = re.sub(r"(?<!^)(?=[A-Z])", "_" , f.read())

print(f_list)