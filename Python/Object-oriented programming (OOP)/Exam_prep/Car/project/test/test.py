from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("Mercedes", "S63", 150, 100)
        self.car2 = SecondHandCar("BMW", "M5", 120, 50)
        self.car3 = SecondHandCar("Mercedes", "S63", 120, 50)

    def test_correct_initialization(self):
        self.assertEqual("Mercedes", self.car.model)
        self.assertEqual("S63", self.car.car_type)
        self.assertEqual(150, self.car.mileage)
        self.assertEqual(100, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_price_lower_than_1(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_price_setter_price_equal_to_1(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_lower_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_mileage_setter_equal_to_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100)

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_new_price_bigger_than_actual_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(120)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successfully(self):
        self.assertEqual(100, self.car.price)

        result = self.car.set_promotional_price(90)

        self.assertEqual(90, self.car.price)

        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_repair_price_too_big(self):
        self.assertEqual(100, self.car.price)
        self.assertEqual([], self.car.repairs)

        half_price = self.car.price / 2

        result = self.car.need_repair(half_price+1, "broken")

        self.assertEqual(100, self.car.price)
        self.assertEqual([], self.car.repairs)

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_price_increased_due_to_repair_charges_exactly_half_price(self):
        self.assertEqual([], self.car.repairs)
        self.assertEqual(100, self.car.price)

        half_price = self.car.price / 2
        current_price = self.car.price

        result = self.car.need_repair(half_price, "broken")

        self.assertEqual(current_price+half_price, self.car.price)
        self.assertEqual(["broken"], self.car.repairs)
        self.assertEqual(1, len(self.car.repairs))

        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_need_repair_price_increased_due_to_repair_charges_less_than_half_price(self):
        self.assertEqual([], self.car.repairs)
        self.assertEqual(100, self.car.price)

        half_price = self.car.price / 2 - 1
        current_price = self.car.price

        result = self.car.need_repair(half_price, "broken")

        self.assertEqual(current_price+half_price, self.car.price)
        self.assertEqual(["broken"], self.car.repairs)
        self.assertEqual(1, len(self.car.repairs))

        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_gt_method_car_type_not_same_as_other_car_type(self):
        result = self.car > self.car2

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_method_car_price_bigger_than_second_car_price(self):
        result = self.car > self.car3
        self.assertTrue(result)

    def test_str_method(self):
        self.car.repairs.append("broken glass")
        self.assertEqual(["broken glass"], self.car.repairs)

        result = self.car.__str__()
        self.assertEqual(f"""Model Mercedes | Type S63 | Milage 150km
Current price: 100.00 | Number of Repairs: 1""", result)


if __name__ == "__main__":
    main()