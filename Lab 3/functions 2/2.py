from Dictionary import movies

def list_above_55():
    list = []
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            list.append(movies[i]["name"])
    print(list)

list_above_55()