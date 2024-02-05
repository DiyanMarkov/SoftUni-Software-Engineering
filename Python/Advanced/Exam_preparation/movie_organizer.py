def movie_organizer(*args):

    genres = {}

    for movie in args:
        name, genre = movie

        if genre not in genres:
            genres[genre] = []

        genres[genre] += [name]

    sorted_collection = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))


    result = ""
    for genre, movies in sorted_collection:
        result += f"{genre} - {len(movies)}\n"

        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result




print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy"))
)


#{'Drama': ['The Godfather', 'The Shawshank Redemption', 'The Pursuit of Happiness'],
# 'Comedy': ['The Hangover', 'The Hangover Part II']}