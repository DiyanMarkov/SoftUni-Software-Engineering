from unittest import TestCase, main

from project import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Nissan", "GTR", 15, 75)

    def test_correct_initialization(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GTR", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_new_value_is_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_new_value_is_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_is_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_try_refuel_with_zero_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_car_with_valid_fuel_amount(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_amount_bigger_than_fuel_capacity(self):
        self.car.refuel(100)

        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_distance_bigger_than_fuel_amount_raises(self):
        distance = 1000

        with self.assertRaises(Exception) as ex:
            self.car.drive(distance)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_distance_with_enough_fuel_amount(self):
        self.car.fuel_amount = 100
        self.car.drive(100)

        self.assertEqual(85, self.car.fuel_amount)

if __name__ == "__main__":
    main()