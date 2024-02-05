from unittest import TestCase, main
from project.extended_list import IntegerList


class IntegerListTests(TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(4,5,6)

    def test_correct_initialization(self):
        self.assertEqual(3, len(self.list.get_data()))
        self.assertEqual(3, len(self.list._IntegerList__data))

    def test_get_data_returns_list_with_the_elements(self):
        self.assertEqual([4,5,6], self.list.get_data())

    def test_adding_non_int_element_to_the_list_raises(self):
        elements = ["abc", False, 6.7, {}, []]

        for value in elements:
            with self.assertRaises(ValueError) as ve:
                self.list.add(value)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_added_element_is_integer_and_append_the_element_to_the_list(self):
        self.assertEqual([4,5,6], self.list.get_data())

        result = self.list.add(7)

        self.assertEqual([4,5,6,7], result)
        self.assertEqual(4, len(self.list.get_data()))

    def test_add_method_get_data_after_addition(self):
        self.list.add(7)
        self.assertEqual([4,5,6,7], self.list.get_data())

    def test_tries_to_remove_bigger_index_raises(self):
        index = 5

        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_tries_to_remove_equal_index_raises(self):
        index = 3

        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_in_range_index_element(self):
        index = 2
        self.assertEqual([4,5,6], self.list.get_data())

        result = self.list.get_data()[index]

        self.assertEqual(6, result)

        self.assertEqual(6, self.list.remove_index(index))
        self.assertEqual([4,5], self.list.get_data())

    def test_remove_return_removed_element(self):
        index = 2

        self.assertEqual(6, self.list.get_data()[index])

    def test_get_index_out_of_range_raises(self):
        index = 5

        with self.assertRaises(IndexError) as ie:
            self.list.get(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_equal_index_out_of_range_raises(self):
        index = 3

        with self.assertRaises(IndexError) as ie:
            self.list.get(index)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_with_valid_index(self):
        index = 0
        self.assertEqual([4, 5, 6], self.list.get_data())

        self.assertEqual(4, self.list.get_data()[index])

        self.assertEqual([4, 5, 6], self.list.get_data())

    def test_insert_element_on_invalid_index_raises(self):
        index = 5
        element = 7

        with self.assertRaises(IndexError) as ie:
            self.list.insert(index, element)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_on_equal_invalid_index_raises(self):
        index = 3
        element = 7

        with self.assertRaises(IndexError) as ie:
            self.list.insert(index, element)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_with_wrong_type_element_raises(self):
        index = 0
        element = "abc"

        with self.assertRaises(ValueError) as ve:
            self.list.insert(index, element)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_element_on_correct_index(self):
        index = 0
        element = 7

        self.assertEqual([4, 5, 6], self.list.get_data())

        self.list.insert(index, element)
        self.assertEqual([7,4,5,6], self.list.get_data())

    def test_get_biggest_method_returns_biggest_element(self):
        self.assertEqual([4, 5, 6], self.list.get_data())

        result = self.list.get_biggest()
        self.assertEqual(6, result)

        self.assertEqual([4, 5, 6], self.list.get_data())

    def test_get_index_with_given_element(self):
        self.assertEqual(1, self.list.get_index(5))

if __name__ == "__main__":
    main()