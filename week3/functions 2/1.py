from Dictionary import movies

def above_55(movie):
    for i in range(len(movies)):
        if movie == movies[i]["name"]:
            if movies[i]["imdb"] > 5.5:
                print(True)
            else:
                print(False)
s = input()

above_55(s)