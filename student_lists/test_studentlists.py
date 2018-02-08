'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''


from student_lists.studentlists import ClassList, StudentError
import unittest
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)



    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')



    ## a test that adds and removes a student, and asserts the student is removed
    # Use assertNotIn
    def test_add_student_then_remove_student(self):
        test_class = ClassList(2)
        test_class.add_student('Yet Another Test Student')
        test_class.remove_student('Yet Another Test Student')
        self.assertNotIn('Yet Another Test Student', test_class.class_list)


    ##a test that removes a student not in the list, and asserts a StudentError is raised

    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student("Not Really here")


    ## a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list(self):
        test_class=ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student("Nobody")



    def test_enrollment_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    ## TODO write a test that adds some example students to an example class, checks
    #cannot complete this item, as I have no idea what I'm supposed to be checking.

    def test_enrollment_empty_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## a test that adds some example students to a test class, call check_enrolled
    # for a student not enrolled, assert check_enrolled returns false
    # #I don't understand.  There is no "check_enrolled".  Used is_enrolled to check.
    def add_students_to_list_check_whether_enrolled(self):
        test_class=ClassList(2)
        test_class.add_student('Kanye West')
        self.assertTrue(test_class.is_enrolled('Taylor Swift'))
        self.assertFalse(test_class.is_enrolled('Not Here'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', test_class.__str__())


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', test_class.__str__())


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))



    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## a test for index_of_student that asserts it returns None if the student is not in the list
    # Cover the cases where the list is empty
    # And, when the list is not empty but does not contain the student name.
    def test_index_of_student_for_absent_name_returning_none(self):
        test_class = ClassList(3)
        self.assertIsNone(test_class.index_of_student('Harry'))
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')
        self.assertIsNone(test_class.index_of_student('Myrtle'))


    ## write a test(s) for your new is_class_full method
    ## Test a case where the class is full, and when it isn't
    def test_is_class_full(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        self.assertFalse(test_class.is_class_full())
        test_class.add_student('Ron')
        self.assertTrue(test_class.is_class_full())


