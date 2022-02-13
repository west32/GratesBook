import unittest
from GradeBook import GradeBook
from Subject import Subject



class GradeBookTest(unittest.TestCase):

    subject=Subject(name="Fizyka")
    second_subject=Subject(name="Matematyka")
    gradebook_with_subject= GradeBook()
    gradebook_with_subject.add_subject(subject)
    gradebook_with_subject.add_subject(second_subject)




    def test_shouldnt_allow_to_add_subject_that_already_exists(self):
        with self.assertRaises(Exception):
            self.gradebook_with_subject.add_subject(self.subject)




    def test_able_to_create_grade_book(self):

        self.assertIsInstance(self.gradebook_with_subject, GradeBook)

    def test_able_to_create_subject(self):

        self.assertIsInstance(self.subject,Subject)

    def test_get_subject_from_grade_book(self):
        self.assertEqual(self.subject.name,self.subject.get_subject())

    def test_add_grade_to_subject(self):
        grade=3.5
        self.gradebook_with_subject.add_subject(self.second_subject)
        self.gradebook_with_subject.add_grade(self.second_subject,grade)

    def test_get_subject_average(self):

        self.gradebook_with_subject.add_grade(self.subject,4)
        self.gradebook_with_subject.add_grade(self.subject,3)
        self.gradebook_with_subject.add_grade(self.subject,5)

        self.assertEquals(4.0,self.subject.get_average_grades())

    def test_get_grade_book_average(self):
        self.gradebook_with_subject.add_grade(self.subject,5)
        self.gradebook_with_subject.add_grade(self.subject,5)
        self.gradebook_with_subject.add_grade(self.second_subject,5)
        self.gradebook_with_subject.add_grade(self.second_subject, 5)
        self.assertEqual(5,self.gradebook_with_subject.add_average())










if __name__ == '__main__':
    unittest.main()
