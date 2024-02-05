from unittest import TestCase, main

from project import Cat


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Roshko")

    def test_correct_initialization(self):
        self.assertEqual("Roshko", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_if_cat_is_not_fed_raises_exception_raises(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_is_not_fed_and_you_feed_it_and_it_gets_sleepy(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_tries_to_sleep_but_can_not_when_it_is_hungry_raises(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_sleeps_successfully_and_is_already_fed(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    main()