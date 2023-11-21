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
    def test_add_returns_correct_result(self):
        """
        Test for add method. Adds the 2 parameters expecting an integer result.
        """
        result = self.calc.add(self.a, self.b)
        self.assertTrue(result == 30)  # correct result
         
    def test_add_returns_integer(self):
        result = self.calc.add(self.a, self.b)
        self.assertEqual(type(result), type(35))  #  Correct data type on result
        
    def test_add_raises_type_error(self):
        """
        Tests if add function raises Type Error if either of values is not an integer.
        """
        self.assertRaises(TypeError, self.calc.add, 10, "19")
    
    # Subtract
    def test_subtract(self):
        result = self.calc.subtract(self.a, self.b)
        self.assertTrue(result == 10)
        self.assertEqual(type(result), type(10))
        
    def test_subtract_raises_type_error(self):
        self.assertRaises(TypeError, self.calc.subtract, 10, "7")
    
    # Multiply
    def test_multiply(self):
        result = self.calc.multiply(self.a, self.b)
        self.assertEqual(result, 200)
        self.assertEqual(type(result), type(200))
        
    def test_multiply_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.multiply(self.a, 12.5)
            self.calc.multiply(13, True)
            self.calc.multiply(13, "14")
    
    # Divide
    def test_divide(self):
        result = self.calc.divide(self.a, self.b)
        self.assertEqual(result, 2)
        self.assertEqual(type(result), type(2.0), msg="Expected result is a integer.")
        
    def test_divide_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(15, 0)
            self.calc.divide(20, 0)
            
    def test_divide_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.divide("12", 19)
            self.calc.divide(True, 12)
            self.calc.divide(12.5, 10.4)
  
if __name__ == '__main__':
    unittest.main()
