import unittest
from GradeBook import GradeBook
from Subject import Subject


class MyTestCase(unittest.TestCase):

	def test_1(self):

		subject = Subject(name="Fizyka")
		gradebook_with_subject = GradeBook()
		gradebook_with_subject.add_subject(subject)

		with self.assertRaises(Exception):
			gradebook_with_subject.add_subject(subject)

if __name__ == '__main__':
	unittest.main()
