import unittest
from cellphones.phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhones = [ testPhone1]
        testAssignmentMgr=PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone1)
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        employee1 = Employee(1, 'Phil')
        employee2 = Employee(2, 'Mary')
        testEmployees=[employee1, employee2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)

        self.assertCountEqual(testEmployees, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        employee1 = Employee(1, 'Phil')
        employee2 = Employee(1, 'Mary')
        testEmployees = [employee1, employee2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(employee2)


    def test_assign_phone_to_employee(self):
        employee2 = Employee(2, 'Mary')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee2)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.assign(2,employee2)
        self.assertEqual(testPhone2,testAssignmentMgr.phone_info(employee2))


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        employee1 = Employee(1, 'Phil')
        employee2 = Employee(2, 'Mary')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.assign(1,employee1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, employee2)

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        employee1 = Employee(1, 'Phil')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.assign(1,employee1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(2, employee1)

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        employee1 = Employee(1, 'Phil')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.assign(1, employee1)
        testAssignmentMgr.assign(1, employee1)  #how do you assert it doesn't raise an error? Doesn't that mean assume it doesn't?


    def test_un_assign_phone(self):
        # Assign a phone, unasign the phone, verify the employee_id is None
        employee1 = Employee(1, 'Phil')

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.assign(1, employee1)
        testAssignmentMgr.un_assign(1)
        self.assertEqual(None, testAssignmentMgr.phone_info(employee1))


    def test_get_phone_info_for_employee(self):
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        employee1 = Employee(1, 'Phil')
        employee2 = Employee(2, 'Mary')
        employee3 = Employee(3, 'Pat')
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.add_employee(employee2)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.assign(1, employee1)
        self.assertEqual(testPhone1, testAssignmentMgr.phone_info(employee1))
        self.assertEqual(None, testAssignmentMgr.phone_info(employee2))
        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(employee3)

