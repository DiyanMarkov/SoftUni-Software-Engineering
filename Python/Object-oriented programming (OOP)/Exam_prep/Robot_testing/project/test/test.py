from unittest import TestCase, main

from project.robot import Robot

class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("123", "Military", 10, 100)
        self.robot2 = Robot("456", "Education", 5, 50)
        self.robot3 = Robot("789", "Education", 10, 100)
        self.robot4 = Robot("101112", "Education", 10, 200)

    def test_class_attributes(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("123", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_invalid_category_raises(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "alabala"

        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_setter_with_negative_price_raises(self):

        with self.assertRaises(ValueError) as ve:
            self.robot.price = - 1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_hardware_already_upgraded_returns(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.robot.hardware_upgrades.append("RAM")
        self.assertEqual(["RAM"], self.robot.hardware_upgrades)

        component_price = 10

        result = self.robot.upgrade("RAM", component_price)

        self.assertEqual("Robot 123 was not upgraded.", result)

        self.assertEqual(["RAM"], self.robot.hardware_upgrades)

    def test_upgrade_successfully(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual(100, self.robot.price)

        component_price = 10
        result = self.robot.upgrade("RAM", component_price)

        self.assertEqual(["RAM"], self.robot.hardware_upgrades)
        self.assertEqual(115, self.robot.price)

        self.assertEqual('Robot 123 was upgraded with RAM.', result)

    def test_update_invalid_data(self):
        self.assertEqual([], self.robot.software_updates)

        self.robot.software_updates.append(1)
        self.robot.software_updates.append(2)

        version = 1.5
        needed_capacity = 20

        self.assertEqual([1,2], self.robot.software_updates)

        result = self.robot.update(version, needed_capacity)

        self.assertEqual([1, 2], self.robot.software_updates)
        self.assertEqual("Robot 123 was not updated.", result)

    def test_update_successfully_with_correct_data(self):
        self.assertEqual([], self.robot.software_updates)
        self.robot.software_updates.append(1)
        self.assertEqual([1], self.robot.software_updates)

        self.assertEqual(10, self.robot.available_capacity)

        version = 1.5
        needed_capacity = 5

        result = self.robot.update(version, needed_capacity)

        self.assertEqual([1, 1.5], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)

        self.assertEqual('Robot 123 was updated to version 1.5.', result)

    def test_gt_first_robot_bigger_price(self):
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 123 is more expensive than Robot with ID 456.', result)

    def test_gt_equal_price(self):
        result = self.robot > self.robot3
        self.assertEqual('Robot with ID 123 costs equal to Robot with ID 789.', result)

    def test_gt_first_robot_smaller_price(self):
        result = self.robot > self.robot4
        self.assertEqual('Robot with ID 123 is cheaper than Robot with ID 101112.', result)


if __name__ == "__main__":
    main()
