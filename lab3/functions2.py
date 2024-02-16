movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_above_5_5(movie):
    return movie["imdb"] > 5.5

def above_5_5_movies(movie_list):
    return list(filter(is_above_5_5, movie_list))

def filter_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

def average_imdb_score(movie_list):
    if not movie_list:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)

def average_imdb_score_by_category(movie_list, category):
    category_movies = filter_by_category(movie_list, category)
    return average_imdb_score(category_movies)

print(is_above_5_5(movies[0]))  

above_5_5_list = above_5_5_movies(movies)
print("Movies with IMDB score above 5.5:", above_5_5_list)

romance_movies = filter_by_category(movies, "Romance")
print("Romance movies:", romance_movies)

average_score_all = average_imdb_score(movies)
print("Average IMDB score of all movies:", average_score_all)

average_score_romance = average_imdb_score_by_category(movies, "Romance")
print("Average IMDB score of Romance movies:", average_score_romance)
