import unittest
# import the mock library
from unittest import mock
# from main import random_func
import main


class TestFileDeletion(unittest.TestCase):
    
    # decorate the test method with the patch function
    # pass the function to be tested
    @mock.patch('main.delete_file')
    # passed the function name as an argument to out test method
    def test_delete_file_success(self, delete_file):
        self.assertTrue(delete_file('dummy.txt')) 
        
        delete_file.assert_called_with('dummy.txt')  # The mock object was called with the arguments given
    
    @mock.patch('main.new_func', return_value=None)   
    def test_new_function(self, new_func):
        self.assertIsNone(new_func())

    @mock.patch('main.random_func', return_value=8)
    def test_random_function(self, random_func):
        # self.assertEqual(random_func(), 6)
        self.assertIn(random_func(), [5, 6, 7, 8, 9, 10])
        
        # Additional assertions
        assert random_func is main.random_func  # The mock is equivalent to the original
        assert random_func.called  # The mock was actually called
        
        random_func.assert_called_with()  # The mock object was called with no arguments
        