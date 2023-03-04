from Dictionary import movies

def IMDB_average(movies):
    sum = 0
    for i in range(len(movies)):
        sum += movies[i]["imdb"]
    print(sum/len(movies))

IMDB_average(movies)