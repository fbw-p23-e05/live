import unittest
from example_2 import divide


class Example2Test(unittest.TestCase):
    
    def test_divide_result(self):
        self.assertEqual(divide(10, 5), 2, msg="The result is not equal to the expected output.")
        
    def test_divide_dt(self):
        self.assertEqual(type(divide(10, 2)), type(5))
        

if __name__ == "__main__":
    unittest.main()
