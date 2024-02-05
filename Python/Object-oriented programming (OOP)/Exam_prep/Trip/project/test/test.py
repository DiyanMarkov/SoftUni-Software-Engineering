from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(10000, 1, False)

    def test_correct_initialization(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, self.trip.DESTINATION_PRICES_PER_PERSON)
        self.assertEqual(4, len(self.trip.DESTINATION_PRICES_PER_PERSON))
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(1, self.trip.travelers)
        self.assertFalse(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_value_smaller_than_1_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_if_travelers_are_family(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(1, self.trip.travelers)

        self.trip.is_family = True

        self.assertFalse(self.trip.is_family)
        self.assertEqual(1, self.trip.travelers)

    def test_book_a_trip_invalid_destination(self):
        result = self.trip.book_a_trip("TRG")

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_successfully_is_family_discount(self):
        self.trip.travelers = 2
        self.trip.is_family = True

        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual({"Bulgaria": 900}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(9100, self.trip.budget)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 9100.00", result)

    def test_book_a_trip_successfully_is_not_family_no_discount(self):
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual({"Bulgaria": 500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(9500, self.trip.budget)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 9500.00", result)

    def test_book_trip_budget_not_enough(self):
        self.trip.travelers = 2
        result = self.trip.book_a_trip("Brazil")

        self.assertEqual('Your budget is not enough!', result)

    def test_booking_status_no_bookings_yet(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.trip.booking_status())
        self.trip.booked_destinations_paid_amounts["Bulgaria"] = 500
        self.trip.booked_destinations_paid_amounts["Brazil"] = 6200

        self.assertEqual({"Bulgaria": 500, "Brazil": 6200},self.trip.booked_destinations_paid_amounts)

        actual = self.trip.booking_status()

        self.assertEqual({"Brazil": 6200, "Bulgaria": 500}, self.trip.booked_destinations_paid_amounts)

        result = []
        self.assertEqual([], result)

        result.append(f"Booked Destination: Brazil")
        result.append(f"Paid Amount: 6200.00")
        result.append(f"Booked Destination: Bulgaria")
        result.append(f"Paid Amount: 500.00")
        result.append(f"Number of Travelers: 1")
        result.append(f"Budget Left: 10000.00")

        expected = "\n".join(result)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()