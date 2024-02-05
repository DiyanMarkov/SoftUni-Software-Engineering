from unittest import TestCase, main

from project import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Ivan", 1000, 10)


    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_with_zero_energy_tries_to_work_raises(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_with_negative_energy_tries_to_work_raises(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_has_enough_energy_to_work(self):
        self.worker.work()

        self.assertEqual(1000, self.worker.money)
        self.assertEqual(9, self.worker.energy)

    def test_worker_energy_improves(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_get_info_method_about_worker(self):
        self.assertEqual("Ivan has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()