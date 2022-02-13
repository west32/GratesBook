import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_shouldnt_allow_to_add_subject_that_already_exists(self):
        self.gradebook_with_subject.add_subject(self.subject)



if __name__=="__main__":
    unittest.main()