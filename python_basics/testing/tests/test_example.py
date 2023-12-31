import unittest  # unitTest module
from example import add  # Unit to be tested
import pytest


class TestExample(unittest.TestCase):
    
    @pytest.mark.add
    def test_add(self):  # Prefix should always be the word 'test'
        result = add(10, 9)
        self.assertEqual(result, 19)
        self.assertEqual(type(result), type(19))


if __name__ == '__main__':
    unittest.main()
    