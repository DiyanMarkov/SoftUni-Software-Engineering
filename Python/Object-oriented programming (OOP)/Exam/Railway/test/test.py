from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("Targovishte")

    def test_correct_initialization(self):
        self.assertEqual("Targovishte", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_setter_raises_equal(self):

        with self.assertRaises(ValueError) as ve:
            self.station.name = "TRG"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_raisesless(self):

        with self.assertRaises(ValueError) as ve:
            self.station.name = "TR"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))


    def test_new_arival_on_board_adds(self):
        self.assertEqual(deque(), self.station.arrival_trains)
        result = self.station.new_arrival_on_board("Fast train")

        self.assertEqual(deque(['Fast train']), self.station.arrival_trains)

    def test_train_has_arrived(self):
        self.assertEqual(deque(), self.station.arrival_trains)
        self.station.arrival_trains.append("Fast train")

        result = self.station.train_has_arrived("Not train")

        self.assertEqual(deque(['Fast train']), self.station.arrival_trains)

        self.assertEqual(f"There are other trains to arrive before Not train.", result)

    def test_has_arrived_departure_trains(self):
        self.assertEqual(deque(), self.station.arrival_trains)
        self.station.arrival_trains.append("Fast train")

        result = self.station.train_has_arrived("Fast train")

        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(['Fast train']), self.station.departure_trains)

        self.assertEqual(f"Fast train is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left(self):
        self.assertEqual(deque(), self.station.departure_trains)
        self.station.departure_trains.append("Fast train")

        result = self.station.train_has_left("Fast train")

        self.assertEqual(deque(), self.station.departure_trains)

        self.assertEqual(True, result)

    def test_train_has_left_false(self):
        self.assertEqual(deque(), self.station.departure_trains)
        self.station.departure_trains.append("Fast train")
        self.assertEqual(deque(['Fast train']), self.station.departure_trains)

        result = self.station.train_has_left("Not fast")

        self.assertEqual(deque(['Fast train']), self.station.departure_trains)

        self.assertEqual(False, result)


if __name__ == "__main__":
    main()