from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        user = next((u for u in self.users_collection if u.username == username), None)

        if user:
            raise Exception("User already exists!")

        existing_user = User(username, age)
        self.users_collection.append(existing_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)

        if not user:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = [m for m in self.movies_collection if m.title == movie.title]

        if existing_movie:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next((u for u in self.users_collection if u.username == username), None)

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = next((u for u in self.users_collection if u.username == username), None)

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        already_liked = [m for m in user.movies_liked if m.title == movie.title]

        if already_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)

        already_liked = [m for m in user.movies_liked if m.title == movie.title]

        if not already_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        if not sorted_movies:
            return "No movies found."

        return "\n".join([m.details() for m in sorted_movies])

    def __str__(self):

        if not self.users_collection:
            result = "All users: No users.\n"

        else:
            users = ", ".join([u.username for u in self.users_collection])
            result = f"All users: {users}\n"

        if not self.movies_collection:
            result += "All movies: No movies."

        else:
            movies = ", ".join([m.title for m in self.movies_collection])
            result += f"All movies: {movies}"

        return result
