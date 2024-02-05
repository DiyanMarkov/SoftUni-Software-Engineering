from unittest import TestCase, main

from project import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Dodo", "Bear", "Rawr")

    def test_correct_initialization(self):
        self.assertEqual("Dodo", self.mammal.name)
        self.assertEqual("Bear", self.mammal.type)
        self.assertEqual("Rawr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Dodo makes Rawr", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Dodo is of type Bear", self.mammal.info())

if __name__ == "__main__":
    main()