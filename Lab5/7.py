import re

f = open("row.txt","r", encoding="utf8")

f_list = re.sub(r"_([a-z])", lambda match: match.group(1).upper() ,f.read())

print(f_list)