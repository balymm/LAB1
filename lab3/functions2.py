# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def above(name):
    for i in range(len(movies)):
        if movies[i]["name"] == name:
            print(movies[i]["imdb"] >= 5.5)

above("We Two")


#2. Write a function that returns a sublist of movies with an IMDB score above 5.5.

def list_above(lst):
    lst_2 = []
    for i in lst:
        for j in range(len(movies)):
            if movies[j]["name"] == i:
                if movies[j]["imdb"] >= 5.5:
                    lst_2.append(i)
    print(lst_2)

list_above(["We Two", "Exam", "Detective", "AlphaJet"])


#3. Write a function that takes a category name and returns just those movies under that category.

def category(categ):
    lst = []
    for i in range(len(movies)):
        if movies[i]["category"] == categ:
            lst.append(movies[i]["name"])
    print(lst)

category("Romance")


#4. Write a function that takes a list of movies and computes the average IMDB score.

def average(lst):
    sum = 0
    count = 0
    for i in lst:
        for j in range(len(movies)):
            if movies[j]["name"] == i:
                sum += movies[j]["imdb"]
                count += 1
    print(sum / count)

average(["We Two", "Exam", "Detective", "AlphaJet"])
# 1 - 7.2, 2 - 4.2, 3 - 7.0, 4 - 3.2 
# 7.2+4.2+7.0+3.2 = 21.6
# 21.6 / 4 = 5.4


#5. Write a function that takes a category and computes the average IMDB score.

def cat_average(cat):
    sum = 0
    count = 0
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            sum += movies[i]["imdb"]
            count += 1
    print(sum / count)

cat_average("Romance")

"""
romance - 'The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two'
imdb - 1-6.2, 2-7.4, 3-6.0, 4 -5.4, 5-7.2
imdb = 32.2
count = 5
32.2 / 5 = 6.44
"""

