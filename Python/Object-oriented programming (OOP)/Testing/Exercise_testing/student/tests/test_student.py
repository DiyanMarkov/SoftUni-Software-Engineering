from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Roshko")
        self.student_with_courses = Student("Ivan", {"python": ["cool"]})

    def test_correct_initialization(self):
        self.assertEqual("Ivan",self.student_with_courses.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"python": ["cool"]},self.student_with_courses.courses)

        self.assertEqual("Roshko", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_and_add_notes_to_existing_course(self):
        result = self.student_with_courses.enroll("python", ["abc", "def"])

        self.assertEqual(["cool", "abc", "def"], self.student_with_courses.courses["python"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_add_empty_course_notes(self):
        result =  self.student.enroll("math", ["abc", "def"])

        self.assertEqual(["abc", "def"], self.student.courses["math"])

        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_notes_to_non_existing_course_with_third_param_Y(self):
        result = self.student.enroll("python db", ["python db is cool"], "Y")

        self.assertEqual(["python db is cool"], self.student.courses["python db"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_adding_new_course(self):
        result = self.student.enroll("math", ["very cool"], "some notes")

        self.assertEqual([], self.student.courses["math"])
        self.assertEqual("Course has been added.", result)

    def test_add_new_notes_in_existing_course(self):
        result = self.student_with_courses.add_notes("python", "abc")

        self.assertEqual(["cool", "abc"], self.student_with_courses.courses["python"])
        self.assertEqual("Notes have been updated", result)

    def test_can_not_add_new_notes_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "abc")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student_with_courses.leave_course("python")
        self.assertEqual("Course has been removed", result)

    def test_can_not_remove_course_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("geometry")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()