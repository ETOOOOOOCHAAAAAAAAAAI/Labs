# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high_score(movie):
    return movie['imdb'] > 5.5


#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def movies_high_score(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]


#Write a function that takes a category name and returns just those movies under that category.
def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]


#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)


#Write a function that takes a category and computes the average IMDB score.
def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    if category_movies:
        return sum(movie['imdb'] for movie in category_movies) / len(category_movies)
    else:
        return 0