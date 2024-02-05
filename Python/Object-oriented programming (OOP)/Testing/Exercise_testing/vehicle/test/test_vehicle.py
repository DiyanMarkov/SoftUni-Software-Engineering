from unittest import TestCase, main

from project import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_attribute_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)


    def test_correct_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel_for_specific_distance_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(20)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel_for_specific_distance_raises(self):
        self.vehicle.drive(10)

        self.assertEqual(8, self.vehicle.fuel)

    def test_refuel_with_too_much_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_capacity(self):
        self.vehicle.capacity = 50

        self.vehicle.refuel(10)

        self.assertEqual(30.5, self.vehicle.fuel)

    def test_str_method(self):
        self.assertEqual("The vehicle has 175.5 "
                         "horse power with 20.5 fuel left and "
                         "1.25 fuel consumption",
                         str(self.vehicle)
                         )



if __name__ == "__main__":
    main()