from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("HP", 2003, 8.5)

    def test_correct_initialization(self):
        self.assertEqual("HP", self.movie.name)
        self.assertEqual(2003, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_is_empty_value_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_is_lower_than_give_one_rases(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1885

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_name_not_in_actors_list(self):
        self.assertEqual([], self.movie.actors)
        name = "Jose"
        self.movie.add_actor(name)
        self.assertIn(name, self.movie.actors)

    def test_add_actor_name_in_actors_list(self):
        self.movie.actors.append("Jose")
        result = self.movie.add_actor("Jose")
        self.assertIn("Jose", self.movie.actors)

        self.assertEqual("Jose is already added in the list of actors!", result)

    def test_greater_than_ratings_our_movie_rating_bigger(self):
        new_movie = Movie("VP", 2008, 6.5)

        result = self.movie > new_movie
        self.assertEqual('"HP" is better than "VP"', result)

    def test_greater_than_ratings_new_movie_rating_bigger(self):
        new_movie = Movie("VP", 2008, 6.5)

        result = new_movie > self.movie
        self.assertEqual('"HP" is better than "VP"', result)

    def test_repr_movie(self):
        self.movie.actors.append("Banderas")
        self.movie.actors.append("Julio Cesar")

        self.assertEqual(
            "Name: HP\n"
            "Year of Release: 2003\n"
            "Rating: 8.50\n"
            "Cast: Banderas, Julio Cesar",
            self.movie.__repr__()
                         )


if __name__ == "__main__":
    main()