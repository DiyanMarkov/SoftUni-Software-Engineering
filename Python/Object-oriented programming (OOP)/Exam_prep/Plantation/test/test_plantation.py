from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_correct_initialization(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative_raises(self):

        with self.assertRaises(ValueError) as ve:
            Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.workers))

        result = self.plantation.hire_worker("John")

        self.assertEqual(["John"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        self.assertEqual("John successfully hired.", result)

    def test_hire_worker_raises(self):
        self.plantation.hire_worker("John")
        self.assertEqual(["John"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("John")

        self.assertEqual("Worker already hired!", str(ve.exception))

        self.assertEqual(["John"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))


    def test_length_plants(self):
        self.plantation.size = 3

        self.plantation.hire_worker("John")
        self.plantation.planting("John", "Rose1")
        self.assertEqual(1, len(self.plantation))

        self.plantation.planting("John", "Rose2")
        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker("Bob")
        self.plantation.planting("Bob", "Rose3")


        self.assertEqual({"John": ["Rose1", "Rose2"], "Bob": ["Rose3"]}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_worker_does_not_exist_raises(self):
        self.plantation.hire_worker("Not existing worker")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("John", "Rose")

        self.assertEqual("Worker with name John is not hired!", str(ve.exception))

    def test_planting_plantation_is_full_raises(self):
        self.plantation.size = 0

        self.plantation.hire_worker("John")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("John", "roses")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting(self):

        self.assertEqual({}, self.plantation.plants)

        self.plantation.hire_worker("John")

        result = self.plantation.planting("John", "Rose")

        self.assertEqual({"John": ["Rose"]}, self.plantation.plants)

        self.assertEqual("John planted it's first Rose.", result)

        result = self.plantation.planting("John", "Rose2")
        self.assertEqual({"John": ["Rose", "Rose2"]}, self.plantation.plants)

        self.assertEqual("John planted Rose2.", result)

    def test_str(self):
        self.plantation.hire_worker("John")
        self.plantation.hire_worker("Bob")

        self.plantation.planting("John", "rose1")
        self.plantation.planting("Bob", "rose2")
        self.plantation.planting("Bob", "rose3")

        result = str(self.plantation)
        expected = f"Plantation size: 10\n" \
                    f"John, Bob\n" \
                    f"John planted: rose1\n" \
                    f"Bob planted: rose2, rose3"

        self.assertEqual(expected, result)

    def test_repr(self):
        self.plantation.hire_worker("John")
        self.plantation.hire_worker("Bob")

        result = repr(self.plantation)

        expected = f"Size: 10\n" \
                   f"Workers: John, Bob"

        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()