import unittest
from calculator import Calculator 


class TestCalculator(unittest.TestCase):
    
    # Run once before the execution of all tests in the test class
    # create calculator object
    @classmethod
    def setUpClass(cls):
        print("SetUpClass was executed.")
    
    # Prepares a test fixture. 
    # Immediately before calling each test method
    def setUp(self):
        self.calc = Calculator()
        # variables for use with calculator
        self.a = 20
        self.b = 10
        
        print("I was executed.")
        
    # Add
    def test_add(self):
        """
        Test for add method. Adds the 2 parameters expecting an integer result.
        """
        self.b = 15
        result = self.calc.add(self.a, self.b)
        self.assertTrue(result == 35)
        self.assertEqual(type(result), type(35))
    
    # Subtract
    def test_subtract(self):
        result = self.calc.subtract(self.a, self.b)
        self.assertTrue(result == 10)
        self.assertEqual(type(result), type(10))
    
    # Multiply
    def test_multiply(self):
        result = self.calc.multiply(self.a, self.b)
        self.assertEqual(result, 200)
        self.assertEqual(type(result), type(200))
    
    # Divide
    def test_divide(self):
        result = self.calc.divide(self.a, self.b)
        self.assertEqual(result, 2)
        self.assertEqual(type(result), type(2.0), msg="Expected result is a integer.")

  
if __name__ == '__main__':
    unittest.main()
