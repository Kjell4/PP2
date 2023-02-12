from Dictionary import movies

def category(c):
    list = []
    for i in range(len(movies)):
        if movies[i]["category"] == c :
            list.append(movies[i]["name"])
    print(list)

cat = input()
category(cat)