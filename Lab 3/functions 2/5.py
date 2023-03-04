from Dictionary import movies

def category_average(c):
    sum = 0
    num = 0
    for i in range(len(movies)):
        if c == movies[i]["category"]:
            sum += movies[i]["imdb"]
            num +=1
    print(sum/num)

cat = input()
category_average(cat)