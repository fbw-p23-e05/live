################################
# Do not modify this file
################################
import unittest
from password_generator_factory import PasswordGeneratorFactory
from password_generator_classes import AlphaGenerator, AlphaNumericGenerator


class TestWarehouseSingleton(unittest.TestCase):
    def setUp(self):
        self.factory = PasswordGeneratorFactory()

    def test_alpha_generator(self):
        alpha_gen = self.factory.create_object("Alpha")
        self.assertIsInstance(alpha_gen, AlphaGenerator, "The factory method doesn't generate an AlphaGenerator correctly")

    def test_alpha_numeric_generator(self):
        alpha_numeric_gen = self.factory.create_object("AlphaNumeric")
        self.assertIsInstance(alpha_numeric_gen, AlphaNumericGenerator, "The factory method doesn't generate an AlphaNumericGenerator correctly")


if __name__ == '__main__':
    unittest.main()

