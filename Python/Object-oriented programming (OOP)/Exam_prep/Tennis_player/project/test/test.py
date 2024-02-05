from unittest import TestCase, main

from project.tennis_player import TennisPlayer

class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Ivan", 20, 50.5)
        self.player2 = TennisPlayer("Gosho", 20, 51.5)
        self.player3 = TennisPlayer("Pesho", 20, 40.5)

    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(50.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_name_less_than_2_symbols_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "G"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_setter_name_equalt_to_2_symbols_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Go"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_player_age_lower_than_18_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 16

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_successful(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win("PL")
        self.assertEqual(["PL"], self.player.wins)

    def test_add_new_win_tournament_has_already_been_added_to_list_of_wins(self):
        self.assertEqual([], self.player.wins)
        self.player.wins.append("PL")
        self.assertEqual(["PL"], self.player.wins)

        result = self.player.add_new_win("PL")
        self.assertEqual(["PL"], self.player.wins)

        self.assertEqual("PL has been already added to the list of wins!", result)

    def test_lt_method_first_player_points_smaller(self):
        result = self.player < self.player2
        self.assertEqual("Gosho is a top seeded player and he/she is better than Ivan", result)

    def test_lt_method_first_player_points_greater(self):
        result = self.player < self.player3
        self.assertEqual("Ivan is a better player than Pesho", result)

    def test_str_method_0_player_wins(self):
        expected = f"Tennis Player: {self.player.name}\n" + \
                    f"Age: {self.player.age}\n" + \
                    f"Points: {self.player.points:.1f}\n" + \
                    f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected, str(self.player))

    def test_str_method_1_player_wins(self):
        self.assertEqual([], self.player.wins)
        self.player.wins.append("PL")
        self.assertEqual(["PL"], self.player.wins)

        expected = f"Tennis Player: {self.player.name}\n" + \
                    f"Age: {self.player.age}\n" + \
                    f"Points: {self.player.points:.1f}\n" + \
                    f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected, str(self.player))

    def test_str_method_2_player_wins(self):
        self.assertEqual([], self.player.wins)
        self.player.wins.append("PL")
        self.player.wins.append("CL")
        self.assertEqual(["PL", "CL"], self.player.wins)

        expected = f"Tennis Player: {self.player.name}\n" + \
                   f"Age: {self.player.age}\n" + \
                   f"Points: {self.player.points:.1f}\n" + \
                   f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(expected, str(self.player))


if __name__ == "__main__":
    main()

