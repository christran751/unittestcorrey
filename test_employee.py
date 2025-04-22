import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    """
    Instead of just always creating an employee object for each individual test case method (over and over)
    We should have a setUp and a tearDown method
    setUp: Creates the necessary setup before each test runs, like initializing the Employee object.
    tearDown: Cleans up after each test case, 
    though it’s not strictly necessary if there’s nothing to clean up
    """
    def setUp(self):
        self.emp = Employee('Adam', 'Willson', 70000)
    
    def tearDown(self):
        del self.emp
    
    def test_email(self):
        self.assertEqual(self.emp.email, 'Adam.Willson@email.com')
    
    def test_fullnamel(self):
        self.assertEqual(self.emp.fullname, 'Adam Willson')
    
    def test_fullname2(self):
        self.emp.first = "Thien"
        self.assertEqual(self.emp.fullname, 'Thien Willson')

    
    def test_raise(self):
        self.emp.apply_raise()
        self.assertEqual(self.emp.pay, 105000)
    
    def test_monthly_schedule(self):
        with patch('employee.request.get') as mocked_get:
            # with patch() and inside path we passed as input w/e we want to mock
            # and we are setting that equal to mocked_get

            # why not import the request into our request and then mock that b/c want to mock the object where they are actually used
            # whenever request.get is run in the employee.py module it will use mocked_get variable
            # instead of the regular get method
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp.monthly_schedule('May')



